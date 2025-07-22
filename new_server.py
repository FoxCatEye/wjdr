from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import json
from datetime import datetime, date
from collections import defaultdict
import re


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """支持多线程的HTTP服务器"""


class RequestHandler(BaseHTTPRequestHandler):
    daily_users = set()
    stats = defaultdict(int)
    last_save_date = date.today()

    # 在RequestHandler类中添加配置热更新支持
    @classmethod
    def reload_config(cls):
        cls._config = cls.get_server_config()
        return cls._config

    @classmethod
    def get_server_config(cls):
        """从version.txt读取服务器配置"""
        config = {"version": "0.0.0", "port": 8080}
        try:
            with open('version.txt', 'r', encoding='utf-8-sig') as f:
                content = f.read()
                # 提取版本号
                version_match = re.search(r'version\s*=\s*([\d.]+)', content)
                if version_match:
                    config["version"] = version_match.group(1)

                # 提取端口号
                port_match = re.search(r'port\s*=\s*(\d+)', content)
                if port_match:
                    config["port"] = int(port_match.group(1))
        except FileNotFoundError:
            pass
        return config

    @classmethod
    def save_daily_stats(cls):
        """保存当日统计并重置计数器"""
        today = date.today().isoformat()
        with open('version.txt', 'a', encoding='utf-8') as f:
            f.write(f"\n# {today} 日活用户: {len(cls.daily_users)}\n")
        cls.daily_users.clear()
        cls.last_save_date = date.today()

    @property
    def VERSION(self):
        return self.get_server_config()["version"]

    '''def log_message(self, format, *args):
        """重写此方法以禁止默认的日志输出"""
        pass'''

    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        # 检查是否需要保存统计
        if date.today() != self.last_save_date:
            self.save_daily_stats()

        if self.path == '/version':
            self._set_headers()
            self.wfile.write(json.dumps({
                "version": self.VERSION, "date": datetime.now().isoformat()
            }).encode())
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        # 检查是否需要保存统计
        if date.today() != self.last_save_date:
            self.save_daily_stats()
        if 'Content-Length' not in self.headers:
            self.send_error(411, "Length Required")
            return

        content_length = int(self.headers['Content-Length'])
        if content_length == 0:
            self.send_error(400, "Empty request body")
            return

        try:
            post_data = self.rfile.read(content_length)
            json_data = json.loads(post_data.decode('utf-8'))  # 明确指定utf-8编码
        except UnicodeDecodeError:
            self.send_error(400, "Invalid encoding")
            return
        except json.JSONDecodeError:
            self.send_error(400, "Invalid JSON format")
            return
        if self.path == '/register':
            client_ip = json_data.get('client_address')  # 从请求体中提取client_address
            today = datetime.now().strftime('%Y-%m-%d')

            if client_ip not in self.daily_users:
                self.daily_users.add(client_ip)
                self.stats[today] = len(self.daily_users)
                print(f"[{datetime.now()}] 新连接: {client_ip} 今日活跃: {self.stats[today]}")

            self._set_headers()
            self.wfile.write(json.dumps({
                "status": "success", "active_users": self.stats[today]
            }).encode())
        else:
            self.send_error(404, "Not Found")


def run():
    config = RequestHandler.get_server_config()
    port = config["port"]

    server = ThreadedHTTPServer(('', port), RequestHandler)
    print(f"服务器运行在端口 {port} (客户端版本: {config['version']})")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("服务器已关闭")


if __name__ == '__main__':
    run()
