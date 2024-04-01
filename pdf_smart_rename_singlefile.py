import os
import fitz  # PyMuPDF
import pytesseract
import requests  # 引入requests
from PIL import Image

def extract_text_from_first_page(pdf_path):
    """从PDF文件的第一页中提取文本。"""
    with fitz.open(pdf_path) as doc:
        if len(doc) > 0:
            page = doc[1]  # 获取第2页
            text = page.get_text()
            if len(text) < 50:  # 假设有效文本至少有50个字符
                # 尝试OCR
                pix = page.get_pixmap()  # 从页面获取像素映射（图像）
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                text = pytesseract.image_to_string(img)
            return text
    return ""
    
def generate_title_with_gemini(pdf_text, api_key):
    """使用Gemini API根据PDF文本内容生成文件标题。"""
    headers = {'Content-Type': 'application/json'}
    prompt = "Suggest a title for the following document content in its original language, if it's a research or science paper, just extract the relevant information and name it like: author&author-publishyear-originaltitle. show el.al for multiple authors:"
    # 将提示和PDF文本内容结合
    full_text = prompt + "\n" + pdf_text
    data = {
        "contents": [{"parts": [{"text": full_text}]}]
    }
    response = requests.post(
        f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}', # 替换为你自己想通过访问的域名
        json=data,
        headers=headers
    )
    print("原始响应:", response.text)  # 调试输出

    if response.status_code != 200:
        print(f"请求失败，状态码：{response.status_code}")
        return ""

    try:
        response_data = response.json()
        if 'candidates' in response_data and len(response_data['candidates']) > 0:
            # 直接提取API响应中的文本内容
            text_content = response_data['candidates'][0]['content']['parts'][0]['text']
            # 由于响应可能包含原始提示信息，你可能需要根据返回的文本格式做进一步的处理来提取实际的标题
            # 这里只是简单地返回整个响应文本，你可能需要根据实际情况进行调整
            return text_content.strip()
        return ""
    except Exception as e:
        print(f"处理API响应时发生错误：{e}")
        return ""


def rename_pdf(pdf_path, api_key):
    """提取PDF文本，使用Gemini生成标题，并重命名PDF文件。"""
    pdf_text = extract_text_from_first_page(pdf_path)
    new_title = generate_title_with_gemini(pdf_text, api_key) + ".pdf"
    new_path = os.path.join(os.path.dirname(pdf_path), new_title)
    if not os.path.exists(new_path):  # 确保不会覆盖已存在的文件
        os.rename(pdf_path, new_path)
        print(f"文件已重命名为: {new_path}")
    else:
        print("已存在同名文件，未执行重命名。")

# 单个PDF文件路径
pdf_file_path = "/Users/summer/Downloads/1.pdf"  # 请替换为你的PDF文件路径
your_api_key = "YOUR_API_KEY_HERE"  # 替换为你的API密钥

rename_pdf(pdf_file_path, your_api_key)
