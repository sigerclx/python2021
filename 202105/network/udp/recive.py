import socket
# 单独收信息

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    local_addr=('',8888)
    udp_socket.bind(local_addr)
    print("Server is running....",local_addr)

    while True:
        revice_data = udp_socket.recvfrom(1024)
        decodestr=revice_data[0].decode('gbk') # windows 按GBK解码
        decodeip = revice_data[1]
        if decodestr=='bye':
            break
        print(decodestr,decodeip)


    udp_socket.close()

if __name__ == '__main__':
    main()