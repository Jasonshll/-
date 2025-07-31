# 智能字幕提取器

一个基于AI技术的本地视频字幕生成器，使用faster-whisper进行语音识别，并集成OLLAMA实现字幕优化。

## 🎯 功能特性

- 🎬 **智能字幕提取**: 基于faster-whisper的精准语音识别
- 🌐 **多语言支持**: 支持中文、英文、日文、韩文等多种语言
- 🤖 **AI字幕优化**: 集成OLLAMA实现智能断句和语义优化
- 📱 **用户友好**: 现代化Web界面，操作简单直观
- ⚡ **高效处理**: 支持批量处理，GPU加速
- 🎨 **多格式输出**: 支持SRT、VTT等多种字幕格式

## 📥 下载使用

### 一键打包版 (不推荐)
- **Windows可执行文件**: [OLLAMA视频翻译助手 v1.0.0](https://github.com/Jasonshll/OllamaVideoTranslator/releases/tag/OLLAMA%E8%A7%86%E9%A2%91%E7%BF%BB%E8%AF%91%E5%8A%A9%E6%89%8Bv1.0)
- 无需安装Python环境，下载即用，但目前版本可能存在很多BUG
- 文件大小: ~400MB (不包含whisper)

### 源码安装
```bash
git clone https://github.com/Jasonshll/OllamaVideoTranslator.git
cd OllamaVideoTranslator
pip install -r requirements.txt
python app.py
```

## 🖥️ 软件截图

![主界面截图](https://raw.githubusercontent.com/Jasonshll/OllamaVideoTranslator/main/主页面截图.png)

## 🚀 快速开始

1. **下载软件**: 从上方链接下载打包版或源码
2. **启动应用**: 双击exe文件或运行`python app.py`
3. **上传视频**: 选择需要处理的视频文件
4. **选择语言**: 设置视频原始语言
5. **开始处理**: 点击"开始提取"按钮
6. **查看结果**: 处理完成后可下载字幕文件

## 🔧 技术栈

- **后端**: Python Flask + faster-whisper
- **前端**: HTML5 + Tailwind CSS + JavaScript
- **AI模型**: OLLAMA本地大语言模型
- **音频处理**: FFmpeg
- **打包工具**: PyInstaller

## 📋 系统要求

- **操作系统**: Windows 10/11
- **内存**: 最少4GB，推荐8GB以上
- **存储**: 至少2GB可用空间
- **网络**: 可选，用于下载模型

## 🤝 贡献指南

欢迎提交Issue和Pull Request来帮助改进项目！

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 📞 联系方式

如有问题，请通过GitHub Issues联系。
