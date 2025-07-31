import requests
import json
import re
import time

def check_ollama():
    """检查OLLAMA服务状态"""
    try:
        response = requests.get('http://localhost:11434/api/tags', timeout=5)
        if response.status_code == 200:
            return {'success': True, 'running': True}
        else:
            return {'success': True, 'running': False}
    except Exception as e:
        return {'success': False, 'error': str(e), 'running': False}

def get_models():
    """获取OLLAMA模型列表"""
    try:
        response = requests.get('http://localhost:11434/api/tags', timeout=10)
        if response.status_code == 200:
            data = response.json()
            models = [model['name'] for model in data.get('models', [])]
            return {'success': True, 'models': models}
        else:
            return {'success': False, 'error': '无法获取模型列表'}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def optimize_subtitles(subtitle_content, model='llama3.2', enable_segment=True, 
                        enable_translate=False, target_language='zh', segment_parts=1,
                        max_sentence_length=30, segment_prompt='', translate_format='srt'):
    """优化字幕内容"""
    try:
        # 解析字幕内容
        segments = parse_subtitle(subtitle_content)
        
        if not segments:
            return {'success': False, 'error': '无法解析字幕内容'}
        
        # 分割字幕为多个部分进行处理
        if segment_parts > 1:
            segment_size = len(segments) // segment_parts
            parts = [segments[i:i+segment_size] for i in range(0, len(segments), segment_size)]
        else:
            parts = [segments]
        
        optimized_parts = []
        
        for part_index, part in enumerate(parts):
            part_text = '\n'.join([seg['text'] for seg in part])
            
            # 构建提示词
            prompt = build_prompt(
                part_text, 
                enable_segment=enable_segment,
                enable_translate=enable_translate,
                target_language=target_language,
                max_sentence_length=max_sentence_length,
                custom_prompt=segment_prompt,
                part_index=part_index + 1,
                total_parts=len(parts)
            )
            
            # 调用OLLAMA
            result = call_ollama(prompt, model)
            
            if result['success']:
                optimized_parts.append(result['content'])
            else:
                return {'success': False, 'error': result['error']}
            
            # 避免请求过快
            time.sleep(1)
        
        # 合并所有部分
        final_content = '\n\n'.join(optimized_parts)
        
        # 格式化输出
        formatted_content = format_output(final_content, translate_format)
        
        return {
            'success': True,
            'content': formatted_content
        }
        
    except Exception as e:
        return {'success': False, 'error': str(e)}

def parse_subtitle(content):
    """解析字幕内容"""
    segments = []
    
    # 尝试解析SRT格式
    if content.strip().startswith('1\n'):
        pattern = r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+?)(?=\n\d+\n|\Z)'
        matches = re.findall(pattern, content, re.DOTALL)
        
        for match in matches:
            segments.append({
                'index': int(match[0]),
                'start': match[1],
                'end': match[2],
                'text': match[3].strip()
            })
    else:
        # 尝试解析纯文本格式
        lines = content.strip().split('\n')
        for i, line in enumerate(lines, 1):
            if line.strip():
                segments.append({
                    'index': i,
                    'start': '',
                    'end': '',
                    'text': line.strip()
                })
    
    return segments

def build_prompt(text, enable_segment=True, enable_translate=False, target_language='zh',
                max_sentence_length=30, custom_prompt='', part_index=1, total_parts=1):
    """构建提示词"""
    
    base_prompt = """你是一个专业的字幕处理专家。请根据要求处理以下字幕内容。

要求：
"""
    
    if enable_segment:
        base_prompt += f"""
1. 智能断句：根据语义和语境合理分割长句，确保每句不超过{max_sentence_length}个字符
2. 语法校正：修正语法错误、错别字和标点符号
3. 保持原意：在断句和校正时保持原意不变
4. 格式规范：确保输出格式为标准的字幕格式
"""
    
    if enable_translate:
        base_prompt += f"""
5. 翻译：将内容翻译成{get_language_name(target_language)}
6. 翻译准确：确保翻译准确、自然、符合语境
"""
    
    if custom_prompt:
        base_prompt += f"""
7. 自定义要求：{custom_prompt}
"""
    
    base_prompt += f"""

处理说明：
- 这是第{part_index}部分，共{total_parts}部分
- 请保持原有时间戳格式不变
- 不要添加额外的解释或注释
- 直接返回处理后的字幕内容

需要处理的字幕内容：
{text}
"""
    
    return base_prompt

def call_ollama(prompt, model):
    """调用OLLAMA API"""
    try:
        url = 'http://localhost:11434/api/generate'
        
        payload = {
            'model': model,
            'prompt': prompt,
            'stream': False,
            'options': {
                'temperature': 0.3,
                'top_p': 0.8
            }
        }
        
        response = requests.post(url, json=payload, timeout=300)
        
        if response.status_code == 200:
            result = response.json()
            return {
                'success': True,
                'content': result.get('response', '').strip()
            }
        else:
            return {
                'success': False,
                'error': f'API请求失败: {response.status_code}'
            }
            
    except requests.exceptions.Timeout:
        return {
            'success': False,
            'error': '请求超时，请检查OLLAMA服务状态'
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def format_output(content, format_type):
    """格式化输出"""
    if format_type == 'srt':
        # 尝试重新格式化为SRT
        lines = content.strip().split('\n')
        formatted_lines = []
        index = 1
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue
                
            # 检查是否是时间戳行
            time_pattern = r'\d{2}:\d{2}:\d{2},\d{3}.*-->.*\d{2}:\d{2}:\d{2},\d{3}'
            if re.match(time_pattern, line):
                formatted_lines.append(str(index))
                formatted_lines.append(line)
                index += 1
                
                # 添加文本行
                text_lines = []
                i += 1
                while i < len(lines) and lines[i].strip() and not re.match(time_pattern, lines[i]):
                    text_lines.append(lines[i].strip())
                    i += 1
                formatted_lines.extend(text_lines)
                formatted_lines.append('')
            else:
                # 处理纯文本格式
                formatted_lines.append(str(index))
                formatted_lines.append(f"{index-1}:00:00,000 --> {index}:00:00,000")
                formatted_lines.append(line)
                formatted_lines.append('')
                index += 1
                i += 1
        
        return '\n'.join(formatted_lines).strip()
    
    return content

def get_language_name(code):
    """获取语言名称"""
    languages = {
        'zh': '中文',
        'en': '英文',
        'ja': '日文',
        'ko': '韩文',
        'fr': '法文',
        'de': '德文',
        'es': '西班牙文',
        'ru': '俄文'
    }
    return languages.get(code, code)