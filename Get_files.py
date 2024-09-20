import sys
import requests

def check_update():
    version_url = "https://12a0f9fa.r7.cpolar.cn/set.ini"
    version = '1.1.0'
    response = requests.get(version_url)
    get_version = response.text.strip()
    last_line = get_version.split("\n")[-1]
    last_version = last_line.replace('version = ', '')
    if last_version != version:
        print('当前版本:%s'%version)
        print("有新版本:%s"%last_version)
        download_update()
    else:
        print("No updates available")
def download_icon():
    update_url = "https://12a0f9fa.r7.cpolar.cn/icon"
    response = requests.get(update_url,stream=True)
    # 确保请求成功
    if response.status_code == 200:
        total_length = response.headers.get('Content-Length')
        if total_length is None:  # 如果Content-Length不可用，可以省略进度显示
            with open('wjdr.exe', 'wb') as f:
                for chunk in response.iter_content(chunk_size=51200):  # 每次读取的数据大小
                    if chunk:  # 过滤掉空的chunk
                        f.write(chunk)
        else:  # 如果Content-Length可用，显示下载进度
            with open('.../wjdr.exe', 'wb') as f:
                downloaded = 0
                total = int(total_length)
                for chunk in response.iter_content(chunk_size=51200):  # 每次读取的数据大小
                    downloaded += len(chunk)
                    f.write(chunk)
                    percentage = (downloaded / total) * 100
                    sys.stdout.write(f"\r下载进度: {percentage:.2f}%")  # 显示下载进度
                    sys.stdout.flush()  # 刷新输出缓冲区，确保进度显示及时更新
                print('下载完成')
    else:
        print(f"无法下载 ，状态码：{response.status_code}")
def download_update():
    update_url = "https://12a0f9fa.r7.cpolar.cn/Wjdr.exe"
    response = requests.get(update_url,stream=True)
    # 确保请求成功
    if response.status_code == 200:
        total_length = response.headers.get('Content-Length')
        if total_length is None:  # 如果Content-Length不可用，可以省略进度显示
            with open('Wjdr.exe', 'wb') as f:
                for chunk in response.iter_content(chunk_size=51200):  # 每次读取1KB数据
                    if chunk:  # 过滤掉空的chunk
                        print(f"Downloading {update_url}")
                        f.write(chunk)
        else:  # 如果Content-Length可用，显示下载进度
            with open('./wjdr.exe', 'wb') as f:
                downloaded = 0
                total = int(total_length)
                print(f"Downloading {update_url}")
                for chunk in response.iter_content(chunk_size=51200):  # 每次读取1KB数据
                    downloaded += len(chunk)
                    f.write(chunk)
                    percentage = (downloaded / total) * 100
                    sys.stdout.write(f"\r下载进度: {percentage:.2f}%")  # 显示下载进度
                    sys.stdout.flush()  # 刷新输出缓冲区，确保进度显示及时更新
                print('下载完成')
    else:
        print(f"无法下载 ，状态码：{response.status_code}")
def download_ini():
    update_url = "https://197fd604.r7.cpolar.cn/wjdr.exe"
    response = requests.get(update_url,stream=True)
    # 确保请求成功
    if response.status_code == 200:
        total_length = response.headers.get('Content-Length')
        if total_length is None:  # 如果Content-Length不可用，可以省略进度显示
            with open('wjdr.exe', 'wb') as f:
                for chunk in response.iter_content(chunk_size=51200):  # 每次读取1KB数据
                    if chunk:  # 过滤掉空的chunk
                        f.write(chunk)
        else:  # 如果Content-Length可用，显示下载进度
            with open('filename.exe', 'wb') as f:
                downloaded = 0
                total = int(total_length)
                for chunk in response.iter_content(chunk_size=51200):  # 每次读取1KB数据
                    downloaded += len(chunk)
                    f.write(chunk)
                    percentage = (downloaded / total) * 100
                    sys.stdout.write(f"\r下载进度: {percentage:.2f}%")  # 显示下载进度
                    sys.stdout.flush()  # 刷新输出缓冲区，确保进度显示及时更新
                print('下载完成')
    else:
        print(f"无法下载 ，状态码：{response.status_code}")

if __name__ == "__main__":
    check_update()