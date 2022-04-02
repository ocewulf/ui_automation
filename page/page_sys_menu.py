#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/3/26 17:49 
"""
from time import sleep
import page
from base.base import Base


class PageSysMenu(Base):
    # 点击一级菜单Banner
    def page_menu_click(self):
        # 点击系统菜单banner
        self.base_click(page.sys_menu_banner)

    # 点击二级菜单Banner
    def page_2nd_menu_click(self):
        # 点击二级菜单Banner
        self.base_click(page.second_menu_banner)

    # 获取首页窗口句柄并切换
    def page_get_homepage(self):
        self.base_get_handle()
        print("当前窗口标题：", self.driver.title)

    # 组合业务方法
    def page_sys_menu(self):
        self.page_menu_click()
        sleep(2)
        self.page_2nd_menu_click()
        sleep(3)
        self.page_get_homepage()