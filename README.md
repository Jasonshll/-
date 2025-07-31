# 智能字幕提取器

一个基于AI技术的本地视频字幕生成器，使用faster-whisper进行语音识别，并集成OLLAMA实现字幕优化。

## 功能特性

- 🎯 **精准识别**：基于faster-whisper的base模型，提供高质量的语音识别
- 🎙️ **人声过滤**：内置人声分离功能，提高字幕提取效果
- 🤖 **AI优化**：集成OLLAMA实现字幕断句、校正与翻译
- 🎨 **美观界面**：现代化的Web UI，支持丝滑的动效体验
- 📱 **响应式设计**：支持桌面和移动设备
- ⚡ **实时进度**：处理进度实时反馈

## 技术栈

- **后端**：Flask + faster-whisper + OLLAMA
- **前端**：Tailwind CSS + FontAwesome + 原生JavaScript
- **音频处理**：FFmpeg
- **AI模型**：Whisper Base模型 + Llama3.2

## 安装指南

### 系统要求

- Python 3.8+
- FFmpeg
- OLLAMA（可选，用于字幕优化）

### 安装步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/Jasonshll/-.git
   cd -
   ```

2. **安装Python依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **安装FFmpeg**
   - Windows: 下载并安装FFmpeg，添加到系统PATH
   - macOS: `brew install ffmpeg`
   - Linux: `sudo apt install ffmpeg`

4. **安装OLLAMA（可选）**
   - 访问 [OLLAMA官网](https://ollama.ai) 下载安装
   - 运行 `ollama pull llama3.2` 下载模型

5. **启动服务**
   ```bash
   python app.py
   ```

6. **访问应用**
   打开浏览器访问：http://localhost:5000

## 使用说明

### 基本使用

1. **上传视频**：拖拽或点击上传区域选择视频文件
2. **配置选项**：
   - 启用OLLAMA优化（需要安装OLLAMA）
   - 选择目标语言（中文、英文、日文、韩文）
3. **开始处理**：点击"开始处理"按钮
4. **下载结果**：处理完成后下载字幕文件

### 文件格式支持

- **视频格式**：MP4、AVI、MKV、MOV、FLV、WMV等
- **输出格式**：SRT字幕文件

## 功能详解

### 人声过滤

系统会自动识别视频中的人声部分，过滤掉背景音乐和环境噪音，提高识别准确率。

### OLLAMA优化

启用后，系统会：
- **智能断句**：根据语义合理分割长句
- **语法校正**：修正语音识别中的语法错误
- **多语言翻译**：支持多种语言之间的翻译

### 实时进度

处理过程分为几个阶段：
1. 提取音频（20%）
2. 人声过滤（40%）
3. 语音识别（60%）
4. 保存字幕（80%）
5. OLLAMA优化（90%）
6. 完成（100%）

## 故障排除

### 常见问题

1. **FFmpeg未找到**
   - 确保FFmpeg已安装并添加到系统PATH
   - 重启应用后重试

2. **OLLAMA连接失败**
   - 检查OLLAMA服务是否启动：`ollama serve`
   - 确认模型已下载：`ollama pull llama3.2`

3. **处理速度慢**
   - 首次运行需要下载模型，请耐心等待
   - 考虑使用GPU加速（需要CUDA支持）

4. **内存不足**
   - 关闭其他占用内存的程序
   - 尝试处理较短的视频

### 性能优化

- **硬件要求**：建议8GB以上内存
- **GPU加速**：安装CUDA和cuDNN可显著提升速度
- **模型选择**：可以修改代码使用更小的模型（如tiny或base）

## 开发指南

### 项目结构

```
项目根目录/
├── app.py                 # 主应用文件
├── ollama_processor.py    # OLLAMA集成模块
├── requirements.txt       # 依赖列表
├── templates/
│   └── index.html        # 前端页面
├── uploads/              # 上传文件目录
└── outputs/              # 输出文件目录
```

### 扩展功能

要添加新的AI模型或功能：
1. 在`ollama_processor.py`中添加新的处理方法
2. 更新前端界面以支持新功能
3. 添加相应的配置选项

## 许可证

MIT License - 详见LICENSE文件

## 贡献

欢迎提交Issue和Pull Request！

## 更新日志

### v1.0.0
- 初始版本发布
- 基础字幕提取功能
- OLLAMA集成优化
- 现代化Web界面