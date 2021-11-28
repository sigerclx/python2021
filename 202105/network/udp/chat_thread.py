import socket,threading
# 用本例子，突破了input的阻塞问题

class SendMsg(threading.Thread):
    def __init__(self,udp_socket):
        threading.Thread.__init__(self)
        self.udp_socket = udp_socket

    def run(self):
        while True:
            send_data = input('请输入信息：')
            self.udp_socket.sendto(send_data.encode('utf-8'), ("127.0.0.1", 8888))

def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print('\n'+str(recv_data[1]),recv_data[0].decode("utf-8"))

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 10086))  # 发送数据端口
    sender  = SendMsg(udp_socket)
    sender.start()
    recv_msg(udp_socket)

if __name__ == '__main__':
    main()