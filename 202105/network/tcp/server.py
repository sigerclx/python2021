import socket
from socket import SOL_SOCKET,SO_REUSEADDR
sk = socket.socket()
sk.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sk.bind(('127.0.0.1',8898))  #把地址绑定到套接字
sk.listen()          #监听链接
print("Server is running...")
conn,addr = sk.accept() #接受客户端链接
ret = conn.recv(1024)  #接收客户端信息
print(ret)       #打印客户端信息
conn.send(b'hi')        #向客户端发送信息
conn.close()       #关闭客户端套接字
sk.close()        #关闭服务器套接字(可选)