import requests
import os

def download_file(url, save_path):
    response = requests.get(url)
    with open(save_path, "wb") as file:
        print(f"Downloading {url}")
        file.write(response.content)



def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        print(f"Folder {folder_path} already exists")


url = "https://12a0f9fa.r7.cpolar.cn/set.ini"  # 替换为你要下载的文件URL
save_folder = "./无尽冬日脚本（电脑版）"  # 替换为你要保存文件的文件夹路径
download_file(url, os.path.join(save_folder,'se.ini'))  # 下载并保存文件到指定文件夹中
