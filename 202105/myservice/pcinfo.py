# encoding=utf-8
# 纯windows Service

"""
pyinstaller -F -c --hiddenimport win32timezone PCInfoService.py

-F 是生成一个独立exe
-c 是控制台程序

生成04_windowsService.exe 后，

可用04_windowsService install 安装服务，在到服务里启动即可

用sc delete 服务名 删除服务
"""
import win32serviceutil
import win32service
import win32event
import os
import io
import logging
import inspect
import servicemanager
import sys
import psutil
import json
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server
import globalvar as gl
import WebAPI


class PythonService(win32serviceutil.ServiceFramework):
    _svc_name_ = "PCInfo"  # 服务名
    _svc_display_name_ = "PC infomation API"  # 服务在windows系统中显示的名称
    _svc_description_ = "Web API is running on port=9999 key=getinfo" + WebAPI.get_time_stamp()  # 服务的描述

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.logger = self._getLogger()
        self.run = True

    def _getLogger(self):
        logger = logging.getLogger('[PythonService]')
        this_file = inspect.getfile(inspect.currentframe())
        dirpath = os.path.abspath(os.path.dirname(this_file))
        handler = logging.FileHandler(os.path.join(dirpath, "service.log"))

        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        WebAPI.recordLog(str(handler))
        logger.setLevel(logging.INFO)

        return logger

    def SvcDoRun(self):
        import time
        global httpd
        global port
        self.logger.info("service is run....")
        WebAPI.recordLog("Service start")

        while self.run:
            print("PC Health " + gl.getvalue('version') + "serving http on port {0}...".format(str(port)))
            WebAPI.recordLog("PC Health " + gl.getvalue(
                'version') + ' ' + WebAPI.get_time_stamp() + "serving http on port {0}...".format(str(port)))
            try:
                httpd.serve_forever()

            except Exception as err:
                WebAPI.recordLog(str(err))
                WebAPI.recordLog('http server error!')
                # httpd.shutdown()

    def SvcStop(self):
        global httpd
        self.logger.info("service is stop....")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.run = False
        WebAPI.recordLog("Service stop ...")
        # 停止http服务
        httpd.shutdown()


if __name__ == '__main__':
    gl.init()
    gl.setvalue('version', 'v0.16')
    port = 9999
    httpd = make_server("0.0.0.0", port, WebAPI.application)

    if len(sys.argv) == 1:
        try:
            evtsrc_dll = os.path.abspath(servicemanager.__file__)
            servicemanager.PrepareToHostSingle(PythonService)
            servicemanager.Initialize('PythonService', evtsrc_dll)
            servicemanager.StartServiceCtrlDispatcher()
        except win32service.error as details:
            WebAPI.recordLog(str(details))
            print(str(details))
            pass
    else:
        win32serviceutil.HandleCommandLine(PythonService)
