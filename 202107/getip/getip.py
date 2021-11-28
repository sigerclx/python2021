from func.getweb.ip import Wanip
import json

ip = Wanip()

txt =ip.getip()

print(txt)