import os
import argparse
import time
from pathlib import Path
import chardet
from google import genai
from prompt_templates import MD_CONVERSION_PROMPT
from config import API_KEY

def detect_encoding(file_path):
    """检测文件的编码格式"""
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def read_file(file_path):
    """读取文件内容，自动检测编码"""
    encoding = detect_encoding(file_path)
    with open(file_path, 'r', encoding=encoding) as f:
        content = f.read()
    return content

def save_as_markdown(content, output_path):
    """将内容保存为markdown文件，使用UTF-8编码"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def convert_to_markdown(text, client, max_retries=3, retry_delay=5):
    """
    使用Gemini API将文本转换为markdown格式
    包含重试机制，应对API调用限制问题
    """
    prompt = MD_CONVERSION_PROMPT + "\n\n" + text
    
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash", 
                contents=prompt
            )
            return response.text
        except Exception as e:
            if attempt < max_retries - 1:  # 如果不是最后一次尝试
                wait_time = retry_delay * (attempt + 1)  # 递增等待时间
                print(f"API调用出错: {e}")
                print(f"等待 {wait_time} 秒后重试... (尝试 {attempt+1}/{max_retries})")
                time.sleep(wait_time)
            else:
                print(f"API调用出错: {e}")
                print(f"已达到最大重试次数 ({max_retries})，转换失败。")
                return None

def process_folder(folder_path, client, delete_original=False):
    """处理指定文件夹中的所有txt文件"""
    folder = Path(folder_path)
    if not folder.exists() or not folder.is_dir():
        print(f"错误: 文件夹 {folder_path} 不存在或不是一个目录")
        return
    
    txt_files = list(folder.glob("*.txt"))
    if not txt_files:
        print(f"警告: 在 {folder_path} 中没有找到txt文件")
        return
    
    print(f"找到 {len(txt_files)} 个txt文件")
    for txt_file in txt_files:
        print(f"处理: {txt_file.name}")
        
        # 读取内容
        content = read_file(txt_file)
        
        # 转换为markdown
        md_content = convert_to_markdown(content, client)
        if md_content:
            # 保存为markdown
            md_file = folder / f"{txt_file.stem}.md"
            save_as_markdown(md_content, md_file)
            print(f"已保存: {md_file.name}")
            
            # 如果指定了删除原始文件，则删除
            if delete_original:
                os.remove(txt_file)
                print(f"已删除原始文件: {txt_file.name}")
        else:
            print(f"转换失败: {txt_file.name}")

def main():
    parser = argparse.ArgumentParser(description='将txt文件智能转换为Markdown格式')
    parser.add_argument('folder', nargs='?', default=None, help='包含txt文件的文件夹路径')
    parser.add_argument('-d', '--delete', action='store_true', help='转换后删除原始txt文件')
    args = parser.parse_args()
    
    # 初始化Gemini客户端
    client = genai.Client(api_key=API_KEY)
    
    # 交互式询问文件夹路径
    folder_path = args.folder
    if not folder_path:
        default_folder = str(Path(__file__).parent / "text_folder")
        user_input = input(f"请输入要转换的文件夹路径 (默认: {default_folder}): ")
        folder_path = user_input.strip() if user_input.strip() else default_folder
    
    # 交互式询问是否删除原始文件
    delete_original = args.delete
    if not args.delete:
        while True:
            user_input = input("是否删除原始txt文件? (y/n, 默认: n): ").strip().lower()
            if user_input in ('y', 'yes'):
                delete_original = True
                break
            elif user_input in ('', 'n', 'no'):
                delete_original = False
                break
            else:
                print("无效输入，请输入 y 或 n")
    
    process_folder(folder_path, client, delete_original)

if __name__ == "__main__":
    main()
