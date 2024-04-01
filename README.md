# PDFs-Smart-Rename
PDFSmartRename 是一个利用OCR和 AI 技术自动重命名 PDF 文件的工具。它通过提取 PDF 文件的第一页文本，使用 Gemini API 生成合适的文件标题，并重命名 PDF 以便更容易识别和管理。

## 特点

- **文本提取**：从PDF文件的第一页提取文本，以确定文件的主要内容。
- **OCR支持**：如果提取的文本不够清晰或文字太少，将使用OCR技术进行图像到文本的转换。
- **AI标题生成**：利用Google的Gemini API根据提取的文本内容自动生成文件标题。
- **批量处理**：支持遍历指定目录下的所有PDF文件，并自动重命名。

## 获取 Gemini API Key

- 打开 [https://makersuite.google.com/](https://makersuite.google.com/)
- 用 Google 账号登录
- 点击 `Get API Key` -> `Create API key in new project` 保存好 key

**注意事项**

- 目前该服务不支持香港IP，[查看支持的区域](https://ai.google.dev/available_regions)
- 由于 IP （如多人共享 IP）或者频率的关系，可能会被谷歌云判定为滥用，导致 API Key 或者 谷歌云账户被禁用，请谨慎使用，或者使用小号。

**防风控**
- 2024-04-01 更新防风控，不再通过 `google-generativeai` 库来访问了，尝试通过自己设置地址访问（用了CF Worker 的默认地址）

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


```
python pdf_smart_rename.py
```

## 注意事项
在使用 PDF-Smart-Rename 进行文件重命名之前，强烈建议对所有待处理的PDF文件进行备份。

## 配置
如果你的Tesseract-OCR没有安装在默认路径，你可能需要在脚本中指定`pytesseract`的路径：

```python
# 配置Tesseract的路径，如果需要的话
pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
```

## 贡献

欢迎通过Pull Requests或Issues提供改进意见和报告错误。

## 许可

该项目使用MIT许可证。有关更多信息，请参阅LICENSE文件。
