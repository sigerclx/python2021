import pandas as pd
import random,os

class Gushi(object):
    def __init__(self,choice):
        self.read(choice)

    def read(self,choice):

        labels = ['title', 'name', 'sentece']
        self.gushi = pd.read_csv(os.path.join('book',choice+'.csv'), names=labels)
        labels = ['name', 'dai']
        self.zuozhe = pd.read_csv('zuozhe.csv', names=labels)

        # for curr_gushi in gushi.itertuples():
        #     print(curr_gushi[0], curr_gushi[1])

        # for i, value in gushi.iterrows():
        #     print(i, value['title'])

    def zuozhe_zhaodai(self,zuozhe):
        #根据作者找出朝代
        try:
            df = self.zuozhe[self.zuozhe['name'] == zuozhe]['dai']
            return list(df)[0]
        except Exception as err:
            #print(err,'找不到作者朝代！')
            return

    def gushi_zuozhe(self,shibody):
        #根据古诗内容，找到作者和诗的题目
        try:
            dfzuozhe = self.gushi[self.gushi['sentece'] == shibody]['name']
            dftitle = self.gushi[self.gushi['sentece'] == shibody]['title']
            return list(dfzuozhe)[0] ,list(dftitle)[0]
        except Exception as err:
            print(err,'找不到古诗！')
            return

    def ramdom_poem(self,numbers=1):
        #随机找出numbers首古诗，含题目、作者、朝代、古诗
        shibody = list(self.gushi['sentece'])
        random.shuffle(shibody)
        questions = []
        for i in range(numbers):
            oneshi =[]
            zuozhe,title = self.gushi_zuozhe(shibody[i])
            chaodai =  self.zuozhe_zhaodai(zuozhe)
            oneshi.append(title)
            oneshi.append(zuozhe)
            oneshi.append(chaodai)
            oneshi.append(shibody[i])
            questions.append(oneshi)

        return questions

    def getfourzuozhe(self,name):
        # 获得包含正确答案的一组4个答案，即四个作者和朝代的结果
        names = []
        line =[]
        #找到作者的朝代
        chaodai = self.zuozhe_zhaodai(name)
        line.append(name)
        line.append(chaodai)
        names.append(line)

        df = self.zuozhe[self.zuozhe['name'] != name]
        df = df.sample(frac=1)[:3]

        for i,value in df.iterrows():
            line = []
            line.append(value['name'])
            line.append(value['dai'])
            names.append(line)
        random.shuffle(names)
        return names