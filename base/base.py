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
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
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

    # 查找方法
    def base_find_elements(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 格式为列表或元组，内容：元素定位信息使用By类
        :param timeout: 查找元素超时时间，默认30s
        :param poll:查找元素频率，默认0.5s
        :return:元素
        """
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))

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

    # 鼠标移入某元素
    def base_move_to_ele(self, loc):
        # 鼠标移入编辑按钮并点击
        ele = self.base_find(loc)
        ActionChains(self.driver).move_to_element(ele).perform()

    # 确认提示框
    def base_confirm(self, loc):
        self.base_click(loc)
        # confirm = self.driver.switch_to.alert()
        # print(confirm.text)
        # sleep(1)
        # confirm.accept()
        # confirm.dismiss()

    # 解析table_content获取下面的tr列表
    def base_get_tr(self, loc):
        table = self.base_find(loc)
        tr_list = table.find_elements(By.TAG_NAME, "tr")
        return tr_list

    # 获取列表全部数据
    def base_get_table_data(self, loc):
        list_1 = []
        list_2 = []
        # 按tr标签定位获取行数
        tr_list = self.base_get_tr(loc)
        # 按行查询表格的数据，取出的数据是一整行
        for tr in tr_list:
            # tr.text获取表格每行的文本内容，切割字符串
            list_2 = tr.text.split()
            # 将返回的文本值列表添加进list2，组合成一个二维列表
            list_1.append(list_2)
        # 以二维列表返回所有文本值
        return list_1

    # 定位并返回要操作的行记录
    def base_find_row(self, loc):
        # 调用获取表格数据函数，获取其列表的返回值信息
        arr_data = self.base_get_table_data(loc)
        for i in range(len(arr_data)):
            for j in range(len(arr_data[i])):
                if arr_data[i][j] == "2022051701M":
                    print("存在要操作的记录")
                    print("坐标/位置为(%r, %r)" % (i + 1, j + 1))
                    return i

    # 解析side_table获取下面的tr列表
    def base_get_tr_side(self, loc, side_table):
        i = self.base_find_row(loc)
        table = self.base_find(side_table)
        tr_list = table.find_elements(By.TAG_NAME, "tr")
        return tr_list[i]

    # 定位要操作的行记录按钮并点击
    def base_click_btn(self, loc, side_table):
        self.base_get_tr_side(loc, side_table)
        # 通过定位的tr行记录查找到操作按钮并点击
        self.base_get_tr_side(loc, side_table).find_element(By.XPATH, ".//a/span[text()='编辑']").click()
        # ActionChains(self.driver).move_to_element(btn).perform()
        # self.base_click()
