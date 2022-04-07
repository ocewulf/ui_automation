#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@File   : .py
@Contact: ocewulf@126.com
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/2/22 15:44   ocewulf      1.0         None
"""
from time import sleep

import allure
from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLogger

log = GetLogger.get_log()


class Base:
    # 初始化
    def __init__(self, driver):
        log.info("正在初始化浏览器：{}".format(driver))
        """浏览器初始化"""
        self.driver = driver

    # 查找方法
    def base_find(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 格式为列表或元组，内容：元素定位信息使用By类
        :param timeout: 查找元素超时时间，默认30s
        :param poll:查找元素频率，默认0.5s
        :return:元素
        """
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 输入方法
    def base_input(self, loc, value):
        """
        :param loc:元素的定位信息
        :param value:输入的值
        """
        # 获取元素
        el = self.base_find(loc)
        # 清空输入栏
        log.info("正在对：{}进行清空操作！".format(loc))
        el.clear()
        # 输入元素
        log.info("正在输入：{}".format(value))
        el.send_keys(value)

    # 点击方法
    def base_click(self, loc):
        # 获取元素并点击
        log.info("正在点击：{}".format(loc))
        self.base_find(loc).click()

    # 获取元素文本
    def base_get_text(self, loc):
        log.info("正在获取文本：{}".format(self.base_find(loc).text))
        return self.base_find(loc).text

    # 截图
    def base_get_img(self):
        log.error("验证失败，正在进行截图！")
        # 调用截图方法截图并保存
        self.driver.get_screenshot_as_file("../image/error.png")
        log.error("验证失败，正在将错误截图写入报告！")
        # 调用截图写入
        sleep(1)
        self.__base_write_img()

    # 截图写入报告(私有)
    def __base_write_img(self):
        # 获取文件流
        with open("../image/error.png", "rb") as f:
            # 使用allure.attach()函数给报告附上截图
            allure.attach(f.read(), "错误原因：", allure.attachment_type.PNG)

    # 获取当前窗口句柄
    def base_get_handle(self):
        # 获取当前窗口和所有窗口的句柄
        # curr_handle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        # 切换至系统主窗口
        main_window = self.driver.switch_to.window(all_handles[-1])
        return main_window
