'''# server.py
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8000

handler = SimpleHTTPRequestHandler
httpd = TCPServer(("", PORT), handler)

print("Server running on port", PORT)
httpd.serve_forever()'''
import cgi
import  http.server
import socketserver
import os
from urllib.parse import unquote

#定义服务器端口
PORT = 8158
#定义文件目录
DIRECTORY = 'C:/Users/ZS-204/Desktop/无尽冬日脚本（电脑版）'
#创建一个处理请求的类
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        #确保返回的路径在指定的目录内
        path = os.path.normpath(os.path.join(DIRECTORY, path.lstrip('/')))
        return path

    '''def do_GET(self):
        try:
            # 对URL进行解码
            path = unquote(self.path[1:])
            # 将路径拼接到服务器根目录
            full_path = os.path.normpath(os.path.join(DIRECTORY, path))

            # 如果路径在服务器根目录之外，则返回404 Not Found
            if not full_path.startswith(os.path.normpath(DIRECTORY)):
                self.send_error(404, "File not found")
                return

            # 如果是目录，则列出目录内容
            if os.path.isdir(full_path):
                self.list_directory(full_path)
                return

            # 如果是文件，则发送文件内容
            if os.path.isfile(full_path):
                with open(full_path, 'rb') as file:
                    self.send_response(200)
                    self.send_header('Content-type', cgi.guess_type(full_path)[0])
                    self.end_headers()
                    self.copyfile(file, self.wfile)
                return
        except Exception as e:
            self.send_error(404, 'File not found: %s' % e)'''

#创建服务器
with socketserver.TCPServer(('', PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    #启动服务器，使其一直运行
    httpd.serve_forever()