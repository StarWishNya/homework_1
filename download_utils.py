import tkinter as tk
import requests
import os

file_path = "data"

#将gbk编码的文件转换为utf-8编码
def encoding(file_path):
    with open(file_path, 'r', encoding='gbk') as f:
        content = f.read()
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return file_path

def download(url, id):
    # 模拟真实浏览器请求头
    headers = {
        'authority': 'dl.wenku8.com',
        'method': 'GET',
        'path': f'/down.php?type=txt&node=1&id={id}',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-GB;q=0.7,en-US;q=0.6,en;q=0.5',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    }

    file_name = f"{id}.txt"
    download_dir = os.path.join(os.path.dirname(__file__), "download")
    os.makedirs(download_dir, exist_ok=True)  # 确保目录存在
    download_path = os.path.join(download_dir, file_name)

    try:
        # 发送 GET 请求
        response = requests.get(url, headers=headers, timeout=10)

        # 检查请求是否成功
        response.raise_for_status()

        # 将响应内容写入文件
        with open(download_path, 'wb') as f:
            f.write(response.content)

        print(f"下载成功：{download_path}")
        encoding(download_path)
        return str(download_path)

    except requests.RequestException as e:
        print(f"下载错误: {e}")
        return None


def download_by_id(id):
    # 使用固定格式生成 URL
    url = f"https://dl.wenku8.com/down.php?type=txt&node=1&id={id}"
    return download(url, id)

def download_click():
    new_window = tk.Toplevel()
    new_window.title("输入ID")
    new_window.geometry("300x150")

    tk.Label(new_window, text="请输入ID:").pack(pady=10)
    id_entry = tk.Entry(new_window)
    id_entry.pack(pady=5)

    def confirm():
        global file_path
        id_value = id_entry.get()
        file_path = download_by_id(id_value)
        new_window.destroy()
        return file_path

    confirm_button = tk.Button(new_window, text="确认", command=confirm)
    confirm_button.pack(pady=10)
    return file_path

