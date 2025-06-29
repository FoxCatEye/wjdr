import http.server
from datetime import datetime
import os
import logging

#logging.disable(logging.CRITICAL)
#logging.getLogger('HTTP/1.1').setLevel(logging.ERROR)

# 用于存储POST请求数据的字典
post_requests = {}
#定义文件目录
DIRECTORY = 'E:\测试文件\测试工具\无尽冬日脚本（电脑版）'
# 自定义的HTTP请求处理类
class SimpleHTTPRequestHandlerWithPost(http.server.SimpleHTTPRequestHandler):
    global post_requests

    def translate_path(self, path):
        # 确保返回的路径在指定的目录内
        path = os.path.normpath(os.path.join(DIRECTORY, path.lstrip('/')))
        return path
    # 重写do_POST方法以保存POST请求数据到字典
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
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
        # 返回200 OK响应
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        #self.wfile.write(b'{"status":"success", "message":"POST request received"}')
def run(server_class=http.server.HTTPServer, handler_class=SimpleHTTPRequestHandlerWithPost):
    global post_requests
    server_address = ('', 8152)  # 服务器监听在0.0.0.0的8000端口
    httpd = server_class(server_address, handler_class)
    print('HTTP server running on port 8152')
    now = datetime.now()
    if now.hour == 0 and now.minute == 0 and now.second == 0:
        # 初始化字典
        post_requests = {}
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping server')

if __name__ == '__main__':
    run()