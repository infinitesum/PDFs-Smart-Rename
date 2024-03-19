import os

import fitz # PyMuPDF

import google.generativeai as genai

import pytesseract

from PIL import Image

  
  

def extract_text_from_first_page(pdf_path):

"""

从PDF文件的第一页中提取文本。

"""

with fitz.open(pdf_path) as doc:

if len(doc) > 0:

page = doc[0] # 获取第1页

text = page.get_text()

if len(text) < 50:

# 尝试OCR

pix = page.get_pixmap() # 从页面获取像素映射（图像）

img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

text = pytesseract.image_to_string(img)

return text

return ""

  

def generate_title_with_gemini(pdf_text, api_key):

"""

使用Gemini API根据PDF文本内容生成文件标题。

"""

# 配置API密钥

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Suggest a title for the following document content in its original language, and if it's a research paper, name it like: author&author-year-title:\n" + pdf_text)

return response.text.strip()

  

def rename_pdf(pdf_path, api_key):

"""

提取PDF文本，使用Gemini生成标题，并重命名PDF文件。

"""

pdf_text = extract_text_from_first_page(pdf_path)

new_title = generate_title_with_gemini(pdf_text, api_key) + ".pdf"

new_path = os.path.join(os.path.dirname(pdf_path), new_title)

if not os.path.exists(new_path): # 确保不会覆盖已存在的文件

os.rename(pdf_path, new_path)

print(f"文件已重命名为: {new_path}")

else:

print("已存在同名文件，未执行重命名。")

  

# 使用示例

# 请替换以下变量中的占位符

your_pdf_path = "/path/to/your/pdf/directory"

your_api_key = "YOUR_API_KEY_HERE"

  

rename_pdf(your_pdf_path, your_api_key)

