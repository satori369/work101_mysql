#!/usr/bin/env python3
"""
webframe
模拟网站的后端应用行为

从httpserver接收具体请求
根据请求进行逻辑处理和数据处理
将需要的数据反馈给httpserver
"""
#kill -9 19099 #杀死后台进程
from socket import *
import json
from multiprocessing import Process
import signal
from settings import *
from urls import *


class Application:
    def __init__(self,frame_ip,frame_port):
        self.s = socket()
        self.s.bind((frame_ip, frame_port))
        self.s.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    #启动服务
    def start(self):
        self.s.listen(5)
        print('Listen the port %d'%frame_port)
        while True:
            c, addr = self.s.accept()
            p = Process(target=self.handle, args=(c,))
            p.daemon = True
            p.start()

    def handle(self,connfd):
        # while True:
        request = connfd.recv(1024).decode()
        request = json.loads(request) #请求字典
        #request=>{'method':'GET','info','xxx'}
        if request['method'] == 'GET':
            if request['info'] == '/' or request['info'][-5:] == '.html':
                response = self.get_html(request['info'])
            else:
                response = self.get_data(request['info'])
        elif request['method'] == 'POST':
            pass
        try:
            # 将结果返回给httpserver
            response = json.dumps(response)
        except:
            connfd.close()
        else:
            connfd.send(response.encode())
            connfd.close()

    def get_html(self, info):
        if info == '/':
            filename = STAIC_DIR + '/index.html'
        else:
            filename = STAIC_DIR + info
        try:
            fd = open(filename)
        except Exception:
            with open(STAIC_DIR+'404.html') as f:
                return {'status':'404','data':f.read()}
        else:
            return {'status':'200','data':fd.read()}

    def get_data(self, info):
        for url,func in urls:
            if url == info:
                return {'status':'200','data':func()}
            return {'status': '200', 'data':'sorry...'}




if __name__ == '__main__':
    app = Application(frame_ip,frame_port)
    app.start()