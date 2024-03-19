# PDF-Smart-Rename
PDFSmartRename 是一个利用OCR和 AI 技术自动重命名 PDF 文件的工具。它通过提取 PDF 文件的第一页文本，使用 Gemini API 生成合适的文件标题，并重命名 PDF 以便更容易识别和管理。

## 特点

- **文本提取**：从PDF文件的第一页提取文本，以确定文件的主要内容。
- **OCR支持**：如果提取的文本不够清晰或文字太少，将使用OCR技术进行图像到文本的转换。
- **AI标题生成**：利用Google的Gemini API根据提取的文本内容自动生成文件标题。
- **批量处理**：支持遍历指定目录下的所有PDF文件，并自动重命名。

## 如何使用

### 环境准备

确保你的系统已安装以下依赖：

- Python 3
- PyMuPDF
- Pillow
- pytesseract
- Google Cloud Platform账号（用于访问Gemini API）

### 安装

1. 克隆仓库到本地：
   ```
   git clone https://github.com/yourusername/PDFSmartRename.git
   ```
2. 进入项目目录，安装所需的Python库：
   ```
   cd PDFSmartRename
   pip install -r requirements.txt
   ```

### 配置

- 在使用OCR功能前，你可能需要配置Tesseract的路径：
  ```python
  pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
  ```
- 确保你有一个有效的Google Cloud Platform API密钥，并替换脚本中的`YOUR_API_KEY_HERE`占位符。

### 使用

- 执行以下命令，开始自动重命名目录下的PDF文件：
  ```
  python pdf_smart_rename.py
  ```

## 贡献

我们欢迎任何形式的贡献，无论是功能请求、bug报告还是代码贡献。请通过GitHub issue或pull request与我们联系。

## 许可

该项目使用MIT许可证。有关更多信息，请参阅LICENSE文件。
