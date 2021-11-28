
image_file = r'c:\1.jpg'
elapse = 2

print("Predict time of %s: %.3fs" % (image_file, elapse))

# 多此一举
print("Predict time of {%s}: {%.3fs}" % (image_file, elapse))

address ='207 N. Defiance St,Archbold,OH'
base ='123'
path = '{}?address={}&sen={}'.format(base,address,'hello')
print(path)

