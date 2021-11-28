import win32serviceutil
import win32service
import win32event
import os
import logging
import inspect


class BackupService(win32serviceutil.ServiceFramework):
    _svc_name_ = "BackupService"
    _svc_display_name_ = "BackupService ClearMedia"
    _svc_description_ = "This is a BackupService of ClearMedia "

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.logger = self._getLogger()
        self.run = True

    def _getLogger(self):
        logger = logging.getLogger('[BackupService]')

        this_file = inspect.getfile(inspect.currentframe())
        dirpath = os.path.abspath(os.path.dirname(this_file))
        handler = logging.FileHandler(os.path.join(dirpath, "service.log"))

        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        return logger

    def SvcDoRun(self):
        import time
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)
        self.logger.info("service is run....")
        while self.run:
            self.logger.info("I am runing....")
            time.sleep(2)
            # fileList = open('log.txt', mode='a', encoding='utf-8')
            # fileList.writelines("111\n")
            # fileList.close()

    def SvcStop(self):
        self.logger.info("service is stop....")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.run = False


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(BackupService)