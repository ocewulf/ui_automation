#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@File   : .py
@Contact: ocewulf@126.com
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/2/22 17:44   ocewulf      1.0         None
"""
from selenium.webdriver.common.by import By
"""配置信息"""
# url地址
url = "http://10.1.93.111/ssohnDist/login"
"""
登录界面元素
"""
# 用户名
username = (By.CSS_SELECTOR, "input[placeholder='用户名']")
# 密码
pwd =(By.CSS_SELECTOR, "input[placeholder='密码']")
# # 验证码
# code = (By.ID, "validcode")
# 登录按钮
login_btn = (By.XPATH, "//*[@id='app']/div/div[1]/div[1]/div/div[2]/button/span")
# 登录名
login_name = (By.XPATH, "//*[@id='app']/div/div[2]/p")
"""
系统菜单界面元素
"""
# 系统主菜单栏
sys_menu_banner = (By.XPATH, "//*[@id='app']/div/div[3]/div/div")
# 二级菜单
second_menu_banner = (By.XPATH, "//*[@id='app']/div/div[5]/div[2]/div/div/div/ul/li/p")
"""
首页菜单栏元素
"""
data_info_menu = (By.XPATH, "//*[@id='app']/section/section/aside/div/ul/div[1]/li/div/p")
hotel_menu = (By.XPATH, "//*[@id='app']/section/section/aside/div/ul/div[1]/li/ul/li[1]/p")