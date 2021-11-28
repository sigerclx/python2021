c = {"a":1,"b":8,"c":6}

for k in c:
    print(c[k])

c1 = {c[i]**2 for i in c if c[i]>4}

print(c1)

student = {
    "喜乐":18,
    "高兴":20,
    "幸福":30
}

k = { key:value for key,value in student.items() if value>19}   #这里要用student.items()
print(k)
k = [ key for key,value in student.items() if value>19]   #这里要用student.items()
print(k)