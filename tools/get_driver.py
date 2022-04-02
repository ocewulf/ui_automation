#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/2/22 18:18 
"""
from selenium import webdriver


class GetDriver:
    # 1.声明变量
    __web_driver = None
    
    # 2.获取driver方法
    @classmethod
    def get_web_driver(cls, url):
        # 判断driver是否为空
        if cls.__web_driver is None:
            # 初始化浏览器
            cls.__web_driver = webdriver.Chrome()
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开url
            cls.__web_driver.get(url)
            # 等待2s
            cls.__web_driver.implicitly_wait(2)
        return cls.__web_driver

    # 3.退出driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver是否为空
        if cls.__web_driver:
            # 退出
            cls.__web_driver.quit()
            # 置空
            cls.__web_driver = None

