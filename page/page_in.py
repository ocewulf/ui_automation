#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@File   : .py
@Contact: ocewulf@126.com
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/2/22 17:22   ocewulf      1.0         None
"""
from page.page_login import PageLogin
from page.page_sys_menu import PageSysMenu


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取PageLogin对象
    def page_get_page_login(self):
        return PageLogin(self.driver)

    # 获取PageSysMenu对象
    def page_get_page_sysmenu(self):
        return PageSysMenu(self.driver)
