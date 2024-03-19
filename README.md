# PDF-Smart-Rename
PDFSmartRename 是一个利用OCR和 AI 技术自动重命名 PDF 文件的工具。它通过提取 PDF 文件的第一页文本，使用 Gemini API 生成合适的文件标题，并重命名 PDF 以便更容易识别和管理。

## 特点

- **文本提取**：从PDF文件的第一页提取文本，以确定文件的主要内容。
- **OCR支持**：如果提取的文本不够清晰或文字太少，将使用OCR技术进行图像到文本的转换。
- **AI标题生成**：利用Google的Gemini API根据提取的文本内容自动生成文件标题。
- **批量处理**：支持遍历指定目录下的所有PDF文件，并自动重命名。


## 安装
本工具依赖于几个关键的Python库：`fitz` (PyMuPDF)、`PIL`、`pytesseract`、以及`google.generativeai`。你可以通过以下命令安装这些依赖项：
```
pip install PyMuPDF Pillow pytesseract google-generativeai-sdk
```
请注意，`pytesseract` 可能还需要你在系统上安装Tesseract-OCR引擎。

## 使用方法

1. 克隆此仓库到本地。
2. 确保你已经获取了必要的API密钥，并且已经安装了所有依赖。
3. 修改脚本中的`directory_path`和`your_api_key`变量，分别设置为你的PDF文件目录和API密钥。
4. 运行脚本。


## 贡献

我们欢迎任何形式的贡献，无论是功能请求、bug报告还是代码贡献。请通过GitHub issue或pull request与我们联系。

## 许可

该项目使用MIT许可证。有关更多信息，请参阅LICENSE文件。
