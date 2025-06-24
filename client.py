import requests
import socket
from requests.exceptions import RequestException
from datetime import datetime


class ClientManager:
    def __init__(self, server_url):
        self.server_url = server_url
        self.session = requests.Session()  # 使用会话保持连接

    def get_public_ip(self):
        """获取公网IP地址"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))  # 使用标准DNS服务器
            client_address = s.getsockname()[0]
            s.close()
            return client_address
        except Exception:
            return '127.0.0.1'

    def register(self):
        """注册客户端到服务器"""
        try:
            headers = {'Content-Type': 'application/json'}
            data = {'client_address': self.get_public_ip(), 'timestamp': datetime.now().isoformat() }
            #response = requests.post("http://fukesihu.gnway.cc:80", data={'key': self.get_public_ip()})
            response = self.session.post(f"{self.server_url}/register", json=data, headers=headers, timeout=3)
            return response.status_code == 200
        except RequestException as e:
            print(f"注册异常: {e}")
            return False

    def check_version(self):
        """检查服务器版本"""
        try:
            response = self.session.get(f"{self.server_url}/version", timeout=3)
            return response.json().get('version')
        except RequestException as e:
            print(f"版本检查失败: {e}")
            return None


if __name__ == '__main__':
    client = ClientManager("http://fukesihu.gnway.cc:80")
    if client.register():
        print("注册成功")
        version = client.check_version()
        if version:
            print(f"服务器版本: {version}")
