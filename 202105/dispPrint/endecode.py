if __name__ == '__main__':
    input_bytes =b'\xff\xfe4\x001\x003\x00'
    input_char =input_bytes.decode('utf-16')
    print(repr(input_char))

    # 按字节写入还是按字符写入文件
    output_char = 'We copy you down,ok?\n'
    output_bytes = output_char.encode('utf-8')
    with open('readme.txt','wb') as f:
        f.write(output_bytes)
    output_char = 'No copy?\n'
    with open('readme.txt','a') as f:
        f.write(output_char)

    f.close()