import socket
import os,time,sys
from multiprocessing import Pool
# 用本例子，没有突破input的阻塞问题

def send_msg(udp_socket):
    while True:
        send_data = input("请输入发送数据：")
        #send_data="1"
        udp_socket.sendto(send_data.encode('utf-8'), ("127.0.0.1", 8888))
        #time.sleep(2)


def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(str(recv_data[1]),recv_data[0].decode("utf-8"))

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 10086))  # 发送数据端口
    ps = Pool(1)  # 最多同时执行2个进程
    #ps.apply_async(send_msg, args=(udp_socket,))  # 异步执行
    ps.apply_async(recv_msg, args=(udp_socket,))
    # 关闭进程池，停止接受其它进程
    ps.close()
    # 阻塞进程
    ps.join()
    print("主进程终止")




if __name__ == '__main__':
    main()