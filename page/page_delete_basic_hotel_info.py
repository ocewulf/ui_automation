#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/5/13 14:15 
"""
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import page
from base.base import Base


class PageDelBasicHotInfo(Base):
    # 点击菜单栏-数据信息-宾馆（酒店）菜单
    def page_click_menubar(self):
        self.base_click(page.data_info_menu)
        self.base_click(page.hotel_menu)

    # 点击健康危害因素调查管理按钮进入宾馆基本情况表界面
    def page_click_hazard_btn(self):
        self.base_click(page.healthy_hazard_btn)

    # 定位至要删除的行记录
    def page_locate_record(self):
        self.base_locate_row(page.table, page.tr_list)

    # 定位并点击要删除的行记录的删除按钮
    def page_click_delete(self):
        self.base_click_delete(page.table, page.tr_list, page.table_rside, page.tr_list, page.del_btn)

    # 定位确认提示框确定按钮并点击
    def page_click_confirm_btn(self):
        self.base_confirm(page.confirm_btn)

    # 组合业务方法
    def page_del_basic_hotel_info(self):
        sleep(1)
        self.page_click_menubar()
        sleep(1)
        self.page_click_hazard_btn()
        sleep(1)
        self.page_locate_record()
        sleep(1)
        self.page_click_delete()
        sleep(1)
        self.page_click_confirm_btn()

