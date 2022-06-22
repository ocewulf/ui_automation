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

    # 输入要删除的问卷编号
    def page_input_id(self, target_id):
        self.base_input(page.query_id, target_id)

    # 点击查询
    def page_click_search(self):
        self.base_click(page.search_btn)

    # 点击删除按钮
    def page_click_delete(self):
        self.base_click(page.del_btn)

    # 定位确认提示框确定按钮并点击
    def page_click_confirm_btn(self):
        self.base_confirm(page.confirm_btn)

    # 组合业务方法
    def page_del_basic_hotel_info(self, target_id):
        sleep(1)
        self.page_click_menubar()
        sleep(1)
        self.page_click_hazard_btn()
        sleep(1)
        self.page_input_id(target_id)
        sleep(1)
        self.page_click_search()
        sleep(1)
        self.page_click_delete()
        sleep(1)
        self.page_click_confirm_btn()
        sleep(2)

    # 组装断言业务方法
    def page_assert_del(self, target_id):
        # 输入问卷编号
        self.base_input(page.query_id, target_id)
        # 点击查询
        self.base_click(page.search_btn)
        # 获取问卷编号
        self.page_get_number()
        # 判断页面是否存在指定的问卷编号 并返回结果
        self.base_elem_is_exist(self.questionaire_id)