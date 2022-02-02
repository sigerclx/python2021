from func.searchengine.search import Search,Mzt
import  time,os
def create_folder(dest_path):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

def two(str):
    if len(str)==1:
        return '0'+str
    else:
        return str

mzt = Mzt()

path = r'pic'

#url,num = mzt.getphotosurl('https://mmzztt.com/photo/')
for k in range(22,37):
    url, num = mzt.getphotosurl('https://mmzztt.com/photo/page/'+str(k))
    photos =[]
    for i in range(0,24,1):
        line = []
        # 单组图的url
        line.append(url[i])
        # 单组图的编号，5位数，用作文件夹名
        line.append(url[i].split(r'/')[-1])
        # 单组图的总张数
        print(num[int(i)])
        line.append(num[int(i)].replace('P', ''))
        photos.append(line)
    print('第',k,'页')
    #print(photos)
    fuhao =['a','b','c','d','e','f','g','h','i']
    #fuhao = ['']
    n = 0
    for pic in photos[0:]:
        n +=1
        print('第',n,'组：')
        url = mzt.getJpgurl(pic[0])
        folder = pic[1]
        currnum = int(pic[2]) + 1
        urlfront = url[:-7]
        #urlfront = url[:-6]

        for i in range(1,currnum+1):
            print('第',k,'页','第',n,'组', i,'/',currnum, '张：')
            for f in fuhao:
                url = urlfront + two(str(i))+f+'.jpg'
                #print(url)
                # 获取文件名称
                create_folder(os.path.join(path,folder))
                filename = os.path.join(path,folder,url.split(r'/')[-1])
                time.sleep(0.25)
                if mzt.download(url, filename)==1:
                    break
                else:
                    print(url, filename, 'can not download .')






