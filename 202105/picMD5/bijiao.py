import filecmp
x= '171.pdf'
y='1711.pdf'

if filecmp.cmp(x, y):
    print(y)