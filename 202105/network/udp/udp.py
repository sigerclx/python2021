import socket
# 单独发信息

def SendMsg(udp_socket):
    while True:
        send_data = input("请输入发送数据：")
        if send_data=='exit':
            break
        udp_socket.sendto(send_data.encode('utf-8'),("127.0.0.1",8888))

        print(send_data)
    udp_socket.close()

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("",7890))  # 发送数据端口
    SendMsg(udp_socket)
    udp_socket.close()


if __name__ == '__main__':
    main()