from enum import Enum

class VIP(Enum):
    Yellow = "hello world"
    Red = 1
    Blue = "passwall"
    Green = 2


vip1  = VIP
print(vip1.Blue.value)

for i in vip1:
    print(i,i.value)
