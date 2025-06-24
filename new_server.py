from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import json
from datetime import datetime
from collections import defaultdict
import re

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """支持多线程的HTTP服务器"""


class RequestHandler(BaseHTTPRequestHandler):
    daily_users = set()
    stats = defaultdict(int)

    @property
    def VERSION(self):
        """从version.txt动态读取版本号"""
        try:
            with open('version.txt', 'r', encoding='utf-8-sig') as f:
                content = f.read()
                match = re.search(r'version\s*=\s*([\d.]+)', content)
                return match.group(1) if match else "0.0.0"
        except FileNotFoundError:
            return "0.0.0"

    def log_message(self, format, *args):
        """重写此方法以禁止默认的日志输出"""
        pass

    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.path == '/version':
            self._set_headers()
            self.wfile.write(json.dumps({
                "version": self.VERSION, "date": datetime.now().isoformat()
            }).encode())
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
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
        #content_length = int(self.headers['Content-Length'])
        #post_data = self.rfile.read(content_length)
        #json_data = json.loads(post_data.decode())
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


def run(port=8152):
    server = ThreadedHTTPServer(('', port), RequestHandler)
    print(f"服务器运行在端口 {port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("服务器已关闭")


if __name__ == '__main__':
    run()
