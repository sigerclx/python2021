# coding:utf-8

import logging
import psutil   
import time
import json
import winreg
import requests
import os
import subprocess
import globalvar as gl
from urllib.parse import parse_qs


logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)   # 加这句话，就是log全部禁止，不加，就可以log打印了

# 定义函数，两个参数，都是python本身定义的，默认就行了。
def application(environ, start_response):
    
    recordLog('start in webapi')
    # 定义文件请求的类型和当前请求成功的code
    try:
        start_response('200 OK', [('Content-Type', 'application/json;charset=utf-8')])
        d = parse_qs(environ['QUERY_STRING'])
        recordLog(environ['QUERY_STRING'])
        key = d.get('key', [''])[0] # 返回第一个age值.
        recordLog(key)
    except Exception as err:
        recordLog('web err!')
        recordLog(str(err))
        
    

    # 获取服务器的硬件运行信息
    if key=='getinfo':
        info=sysInfo()
        json_str = json.dumps(info,ensure_ascii=False,indent=4)
        recordLog('record getinfo')
        return [json_str.encode('utf-8')]
    
    # 主动触发服务器下载最新版的热更新
    elif key=='download':
        info = {"status": "download"}
        try:
            res =requests.get(r'http://47.75.120.191:83/PCInfoService.exe',timeout=30)
        except Exception as err:
            info = {"status":str(err)}
            recordLog(str(err))

        down=os.path.join(getPath(),'PCInfoService.exe')

        try:
            downloadFile = open(down,'wb')
            for chunk in res.iter_content(100000):
                downloadFile.write(chunk)
            #recordLog(os.path.getsize(downloadFile))
            downloadFile.close()
            info = {"status":"download finish"}

            recordLog("download finish")
            
            WriteRestartCmd()
            recordLog("update Start")
            recordLog("shutdown")
          
        except Exception as err:
            recordLog(str(err))
            info = {"status":str(err)}
            
        finally:
            return [json_str.encode('utf-8')]
        
    else:
        logging.debug('Noget')
        info = {"status": "可以使用 ?key=getinfo 获取电脑的cpu 等信息"}
        json_str = json.dumps(info,ensure_ascii=False,indent=4)
        return [json_str.encode('utf-8')]
   
#编写bat脚本，删除旧程序，运行新程序
def WriteRestartCmd():
    os.chdir(getPath())
    b = open("upgrade.bat",'w')
    TempList = "@echo off\n";   #关闭bat脚本的输出
    TempList += "if not exist pcinfoservice.exe exit \n";    #新文件不存在,退出脚本执行
    TempList += "sc stop pcinfo \n" 
    TempList += "ping /n 5 127.1>nul \n"   #5秒后删除旧程序（3秒后程序已运行结束，不延时的话，会提示被占用，无法删除）
    TempList += "del PCInfo.exe /q \n"
    TempList += "ren PCInfoService.exe PCInfo.exe \n"
    TempList += "pcinfo.exe install \n"
    TempList += "sc start pcinfo \n"
    TempList += "sc config pcinfo start= auto"  
    b.write(TempList)
    b.close()
    subprocess.Popen("upgrade.bat")


def recordLog(strmsg): #把strmsg写入日志
    
    os.chdir(getPath())
    try:
        logFile = open(r'web.log','a')
        logFile.write(get_time_stamp()+'  ') #写入日志
        logFile.write(strmsg+'\n')
    except Exception as err:
        logFile.write(get_time_stamp()+'  ') #写入日志
        logFile.write('write web.log err!\n')
        pass
    finally:
        logFile.close()
    return

def sysInfo():
    info={}
    
    line={}
    line.setdefault('CPU核心',str(psutil.cpu_count()))
    line.setdefault('CPU利用率',str(int(psutil.cpu_percent())) + '%')
    info['CPU']=line

    line={}
    line.setdefault('空闲内存G',str(round(psutil.virtual_memory().free/(1024.0*1024.0*1024.0), 2)))
    line.setdefault('总内存G',str(int(round(psutil.virtual_memory().total/(1024.0*1024.0*1024.0)))))
    line.setdefault('内存利用率',str(int((psutil.virtual_memory().total-psutil.virtual_memory().free)/float(psutil.virtual_memory().total)*100))+ '%')
    info['Memory'] =line
    	
    line={}
    
    io = psutil.disk_partitions()
    j=0
    for i in io:
        diskstr=[]
        try:
            o = psutil.disk_usage(i.device)
        except Exception as err:
            logFile = open(r'web.log','a')
            logFile.write(get_time_stamp()+'  ') #写入日志
            logFile.write(str(err)+'\n') #写入日志
            logFile.close()
            j+=1
            continue
            
        disk=io[j][0].strip(r':\\')
        diskstr.append(str(int(o.free/(1024.0*1024.0*1024.0)))+"G")
        diskstr.append(str(int(o.total/(1024.0*1024.0*1024.0)))+"G") 
        line.setdefault(disk,diskstr)
        del(diskstr)
        j+=1

    info['Disk']=line
    try:
        info.setdefault('version',gl.getvalue('version'))
    except Exception as err:
        recordLog("version write err")
        
    return info

def getPath():
    #获取服务执行程序的路径
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Services\PCInfo")
        downloadPath =winreg.QueryValueEx(key,"ImagePath")
        path=os.path.dirname(downloadPath[0][1:])
    except Exception as err:
        path=r'c:\windows\system32'
        recordLog('Path change err: '+ str(err))
    return path


def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp
