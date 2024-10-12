import  http.server
import socketserver
import os
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
#创建服务器
with socketserver.TCPServer(('', PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    #启动服务器，使其一直运行
    httpd.serve_forever()