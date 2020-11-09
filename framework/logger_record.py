#_*_coding:utf-8_*_
import logging
from os.path import dirname, abspath
import time


class LoggerRecord(object):
    def __init__(self, logger):
        '''#创建日志收集器
        self.logger = logging.getLogger(logger)
        #设置日志收集器等级
        self.logger.setLevel(logging.DEBUG)

        #定义日志输出格式
        #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        #创建一个handler，定义日志文件，用于写入日志文件
        rg = time.strftime("%Y%m%d%H%m%S", time.localtime(time.time()))
        log_path = dirname(abspath('.')) + '\logs\\'
        log_name = log_path + rg + '.log'

        fh = logging.FileHandler(log_name)

        #将日志格式写入到日志文件中
        fh.setFormatter(formatter)

        #定义输出到日志文件的日志等级
        fh.setLevel(logging.INFO)

        #把输出到文件，添加到日志收集器中
        self.logger.addHandler(fh)

        #创建一个handler，定义日志输出到控制台
        #定义输出到控制台
        output_console = logging.StreamHandler()
        #设置输出到控制台的日志格式
        output_console.setFormatter(formatter)
        #设置输出到控制台的日志等级
        output_console.setLevel(logging.INFO)
        #把输出到控制台的日志，添加到日志收集器中
        self.logger.addHandler(output_console)'''

        #使用basinConfig创建日志
        self.logger = logging.getLogger(logger)

        #创建日志文件
        rg = time.strftime("%Y%m%d%H%m%S", time.localtime(time.time()))
        log_path = dirname(abspath('.')) + '\logs\\'
        log_name = log_path + rg + '.log'

        LOG_FORMATE = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        DATE_FORMATE = "%Y-%m-%d %H:%M:%S"
        fp = logging.FileHandler(log_name)
        fs = logging.StreamHandler()
        handler = logging.basicConfig(level=logging.DEBUG, format=LOG_FORMATE, datefmt=DATE_FORMATE, handlers=[fp, fs])
        self.logger.addHandler(handler)

    def getlog(self):
        return self.logger