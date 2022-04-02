import unittest
import logging
import logging.handlers
import time
import os.path


class Logger(object):
    def __init__(self, logger):
        """指定保存日志文件的路径、级别、以及调用文件
        将日志存入指定文件"""
        # 创建一个日志器logger，并设置日志级别为debug
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler,写入日志文件
        date = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath('../config')) + '/log'
        log_name = log_path + date + '.log'
        # 创建一个文件处理器handler并设置其日期级别为INFO
        filehandler = logging.handlers.RotatingFileHandler(log_name, maxBytes=1024 * 1024, backupCount=5, encoding='utf-8')
        filehandler.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        # 创建一个流处理器handler并设置其日志级别为INFO
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        # 创建一个格式器formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        filehandler.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给日志处理器logger添加上面创建的handler
        self.logger.addHandler(filehandler)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
