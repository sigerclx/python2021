from func.ini import readIni,writeIni
# 读取InI文件的例子

#读
info  = readIni('info','pc')
print(info)

info  = readIni('info','system')
print(info)

# 写入
writeIni('system','os2',group='info')

info  = readIni('info','system')
print(info)