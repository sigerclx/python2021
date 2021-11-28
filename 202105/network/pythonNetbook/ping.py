import socket
if __name__ == '__main__':
    hostname ='www.baidu.com'
    addr = socket.gethostbyname(hostname)
    print('The ip address of %s is %s' % (hostname,addr))