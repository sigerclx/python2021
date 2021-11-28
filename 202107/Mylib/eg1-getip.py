from func.getweb.ip import Wanip

# 获取公网IPv4
ip = Wanip()
iptxt = ip.getip()
print(iptxt)