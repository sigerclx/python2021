import datetime
import time
import os,configparser
import glob
import sys



def search_word_mean(word):
    conn = Get_value('conn')
    cursor = conn.cursor()

    edit_SQL="select mean from english where word=\'%s\'" % (word)
    cursor.execute(edit_SQL)
    aa =cursor.fetchall()
    cursor.close()
    #print('word :=',word)
    if not aa or aa==[] or aa==None:
        #print('word :====', word)
        mean = downloadMean(word)
        #print("no this word mean：",word)
        return mean
    aa = aa[0][0]
    aa = aa.replace('#','\'')
    try:
        wordmean = eval(aa)
    except Exception as err:
        print("tools.py 函数 search_word_mean ",word,err)
        Set_value('conn',None)
        sys.exit(1)

    return wordmean

def downloadMean(word):

    mean = str(getwordMean(word))

    if not mean or mean=='None':
        print('下载不到单词: \' %s \' 的含义，请自己补充，也可能是拼写错误。' % (word))
        Set_value('conn', None)
        sys.exit(1)

    conn = Get_value('conn')
    cursor = conn.cursor()
    # access数据库里不能存储 ' 符号,需要替换为"
    edit_SQL = "insert into english ([word],[mean])  values('%s','%s')" % (word, mean.replace("\'", "#"))
    try:
        cursor.execute(edit_SQL)
        cursor.commit()
    except Exception as err:
        print(err)
        Set_value('conn', None)
        cursor.close()
        sys.exit(1)
    cursor.close()
    print("下载单词\' %s\'的含义, 补充到数据库." %  (word))
    try:
        mean = eval(mean)
    except Exception as err:
        print("tools.py 函数 downloadMean ",word,err)
        Set_value('conn',None)
        sys.exit(1)

    return mean



def recordLog(strmsg,filename='answer.log'): #把strmsg写入日志
    try:
        logFile = open(filename,'a')
        logFile.write(get_time_stamp()+'  ') #写入日志
        logFile.write(strmsg+'\n')
    except Exception as err:
        logFile.write(get_time_stamp()+'  ') #写入日志
        logFile.write('log write err:'+str(err)+'\n')
        pass
    finally:
        logFile.close()
    return

#获得当前日期
def get_day():
    ct = time.time()
    local_time = time.localtime(ct)
    hourtime = time.strftime("%Y-%m-%d", local_time)
    return hourtime

#比较两个日期
def day_cmp(first_time, second_time):
    
    if (first_time==0) or (second_time==0):
        return 0
    #if first_time<second_time:
    #   first_time, second_time = second_time, first_time
    return (datetime.datetime.strptime(first_time,"%Y-%m-%d") - datetime.datetime.strptime(second_time,"%Y-%m-%d")).days


def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp

def get_hour():
    ct = time.time()
    local_time = time.localtime(ct)
    hourtime = time.strftime("%H:%M:%S", local_time)
    return hourtime	

def time_cmp(first_time, second_time):
    
    if (first_time==0) or (second_time==0):
        return 0
    if first_time<second_time:
       first_time, second_time = second_time, first_time
    return (datetime.datetime.strptime(first_time,"%H:%M:%S") - datetime.datetime.strptime(second_time,"%H:%M:%S")).seconds


def get_seconds(t1,t2):
    return  round((t2 - t1).total_seconds(), 2)


# 获取目录文件列表,如果传递进来是一个文件也可以
def Get_file_list(source_path):
    files_list=[]
    if os.path.isfile(source_path):
        files_list.append(source_path)
        return files_list

    for i in glob.glob(source_path + '/**/*', recursive=True):
        if os.path.isfile(i):
            files_list.append(i)
    return files_list

def writelisttohtml(mylist,htmlfile):
    #htmlfile = configRead.readConfig('parameter','webfile')

    try:
        webUrlFile=open(htmlfile,'w',encoding='utf-8')
    except Exception as err:
        recordLog(str(err))
        return
        
    try:
        webUrlFile.write(r'''
                
    <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                </head>
                <style type=text/css>
                table.gridtable
                        {
                                font-family: verdana,arial,sans-serif;
                                font-size:14px;
                                color:#333333;
                                border-width: 1px;
                                border-color: #666666;
                        }
                table.gridtable th {
                                border-width: 1px;
                                padding: 1px;
                                border-style: solid;
                                border-color: #666666;
                                background-color: #dedede;
                        }
                table.gridtable td {
                                border-width: 1px;
                                padding: 6px;
                                border-style: solid;
                                border-color: #666666;
                                background-color: #ffffff;}
                                
                </style>''')

        webUrlFile.write('<h2>'+get_time_stamp()+'</h2>\n')
        webUrlFile.write('\n<table class=gridtable align=\'left\'>\n')

        for t1 in mylist:
                webUrlFile.write('<tr>')
                for t2 in t1:
                        webUrlFile.write('<td>'+str(t2)+'</td>')
                webUrlFile.write('<tr>\n')
        webUrlFile.write('</table>')
    except Exception as err:
            recordLog("write to html error")
            recordLog(str(err))
    finally:
            webUrlFile.close()

def readConfig(group,key):
    cp = configparser.SafeConfigParser()
    value =""
    try:
        cp.read('config.ini',encoding='utf-8')
        value = eval(cp.get(group,key))
    except Exception as err:
        print("read config err!"+ str(err))
    return  value


#a1='17:05:05'
#a2=get_hour()
#print(time_cmp(a1,a2))
