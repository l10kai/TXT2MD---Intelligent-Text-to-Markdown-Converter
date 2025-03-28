# TXT2MD - Intelligent Text to Markdown Converter

TXT2MD is an intelligent text file conversion tool that leverages Google's Gemini AI to transform plain text files into well-formatted Markdown documents.

[中文文档](#txt2md---智能文本转markdown转换器)

## Features

- Automatically converts plain text to structured Markdown format
- Intelligently recognizes and formats headings, lists, code blocks, etc.
- Handles file encoding detection and conversion to UTF-8
- Batch processes multiple files in a folder
- Optional removal of original text files after conversion
- Built-in retry mechanism for API rate limiting

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/txt2md.git
cd txt2md
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your Google Gemini API key in `config.py`

> **IMPORTANT:** This project requires a Google Gemini API key. You can apply for one at [Google AI Studio](https://aistudio.google.com/). Support for additional APIs may be added in future updates.

## Usage

### Command Line Interface

```bash
python txt_to_md.py [folder_path] [-d]
```

Options:
- `folder_path`: Path to the folder containing .txt files (optional)
- `-d, --delete`: Delete original .txt files after conversion (optional)

If no folder path is provided, the program will interactively prompt for input.

### Interactive Mode

Simply run the script without arguments for interactive prompts:

```bash
python txt_to_md.py
```

The program will ask for:
1. The folder path to process (with a default suggestion)
2. Whether to delete original files after conversion

## Dependencies

- Python 3.6+
- google-generativeai
- chardet

## Example

Before:
```
WEB服务器和FTP服务器

WEB服务器
1.WEB服务器也称为网页服务器或HTTP服务器
...
```

After:
```markdown
# WEB服务器和FTP服务器

## WEB服务器
1. WEB服务器也称为网页服务器或HTTP服务器
...
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

# TXT2MD - 智能文本转Markdown转换器

TXT2MD是一个智能文本文件转换工具，利用Google的Gemini AI将纯文本文件转换为格式良好的Markdown文档。

[English Documentation](#txt2md---intelligent-text-to-markdown-converter)

## 功能特点

- 自动将纯文本转换为结构化的Markdown格式
- 智能识别并格式化标题、列表、代码块等
- 自动检测文件编码并转换为UTF-8
- 批量处理文件夹中的多个文件
- 可选择在转换后删除原始文本文件
- 内置API访问限制的重试机制

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/txt2md.git
cd txt2md
```

2. 安装所需依赖：
```bash
pip install -r requirements.txt
```

3. 在`config.py`中配置您的Google Gemini API密钥

> **重要说明：** 本项目需要自备Google Gemini API密钥，可在 [Google AI Studio](https://aistudio.google.com/) 上申请。后续可能会更新支持其他API。

## 使用方法

### 命令行界面

```bash
python txt_to_md.py [文件夹路径] [-d]
```

选项：
- `文件夹路径`：包含.txt文件的文件夹路径（可选）
- `-d, --delete`：转换后删除原始.txt文件（可选）

如果未提供文件夹路径，程序将交互式地提示输入。

### 交互模式

无需参数直接运行脚本即可使用交互式提示：

```bash
python txt_to_md.py
```

程序将询问：
1. 要处理的文件夹路径（带有默认建议）
2. 转换后是否删除原始文件

## 依赖项

- Python 3.6+
- google-generativeai
- chardet

## 示例

转换前：
```
WEB服务器和FTP服务器

WEB服务器
1.WEB服务器也称为网页服务器或HTTP服务器
...
```

转换后：
```markdown
# WEB服务器和FTP服务器

## WEB服务器
1. WEB服务器也称为网页服务器或HTTP服务器
...
```

## 许可证

该项目采用MIT许可证 - 详情请参阅LICENSE文件。
