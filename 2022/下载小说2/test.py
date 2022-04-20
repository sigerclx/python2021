import os
dest_path = r'三寸人间.txt'
name ='三寸人间/1400'
userinput = name.split('/')
print(userinput)

if os.path.exists(dest_path):
    print('yes')
else:
    print('no')