import os

import fitz # PyMuPDF

import google.generativeai as genai

import pytesseract

from PIL import Image

  

# 配置Tesseract的路径，如果需要的话

# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'

  
  

def extract_text_from_first_page(pdf_path):

"""

从PDF文件的第一页中提取文本。

"""

with fitz.open(pdf_path) as doc:

if len(doc) > 0:

page = doc[0] # 获取第一页

text = page.get_text()

if len(text) < 50: # 假设有效文本至少有50个字符

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

  

def rename_pdfs_in_directory(directory_path, api_key):

"""

遍历指定目录中的所有PDF文件，并尝试重命名它们。

"""

for filename in os.listdir(directory_path):

if filename.lower().endswith('.pdf'):

pdf_path = os.path.join(directory_path, filename)

print(f"处理文件：{pdf_path}")

try:

rename_pdf(pdf_path, api_key)

except Exception as e:

print(f"处理文件 {pdf_path} 时发生错误：{e}")

  

# 批量重命名目录下的PDF文件

# 请替换以下变量中的占位符

  

directory_path = "/path/to/your/pdf/directory" # 替换为你的PDF文件目录

your_api_key = "YOUR_API_KEY_HERE" # 替换为你的API密钥

  

rename_pdfs_in_directory(directory_path, your_api_key)
