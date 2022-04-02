#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/2/23 17:31 
"""
# 导包
import logging.handlers
import os
from config import BASE_PATH


# 新建日志器类
class GetLogger:
    # 新建日志器变量
    __log = None

    # 获取日志器的方法
    @classmethod
    def get_log(cls):
        # 判断日志器为空：
        if cls.__log is None:
            # 获取日志器
            cls.__log = logging.getLogger()
            # 设置日志级别
            cls.__log.setLevel(logging.INFO)
            # 设置日志文件路径
            log_path = BASE_PATH + "log" + os.sep + "test.log"
            # 获取处理器
            th = logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                           when='midnight',
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8')
            fmt = '%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
            # 获取格式器
            fm = logging.Formatter(fmt)
            # 添加格式器至处理器
            th.setFormatter(fm)
            # 添加处理器至日志器中
            cls.__log.addHandler(th)
        # 返回日志器
        return cls.__log


if __name__ == '__main__':
    log = GetLogger.get_log()
    log.info("测试信息级别日志")
    log.error("测试错误级别日志")
