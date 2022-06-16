#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/6/10 11:56 
"""
from time import sleep

import page
from base.base import Base


class PageSubmit(Base):
    # 点击菜单
    def page_click_menubar(self):
        # 点击一级菜单-数据信息
        self.base_click(page.data_info_menu)
        # 点击二级菜单-宾馆（酒店）
        self.base_click(page.hotel_menu)

    # 点击健康危害因素调查管理
    def page_click_harzard_btn(self):
        self.base_click(page.healthy_hazard_btn)

    # 点击数据状态并选择状态‘未提交’
    def page_click_status(self):
        self.base_click(page.data_status)
        sleep(1)
        self.base_click(page.data_status_unsubmit)

    # 输入问卷编号
    def page_input_id(self, target_id):
        self.base_input(page.questionaire_id, target_id)

    # 点击查询
    def page_click_search(self):
        self.base_click(page.search_btn)

    # 获取问卷编号
    def page_get_number(self):
        return self.base_get_text(page.questionaire_no)

    # 勾选checkbox
    def page_check_record(self):
        # 定位要操作的行记录勾选框并点击
        self.base_click(page.check_box)

    # 点击提交按钮
    def page_click_submit(self):
        self.base_click(page.submit_btn)

    # 组合业务方法
    def page_submit(self, target_id):
        self.page_click_menubar()
        sleep(1)
        self.page_click_harzard_btn()
        sleep(2)
        self.page_click_status()
        sleep(1)
        self.page_input_id(target_id)
        sleep(1)
        self.page_click_search()
        sleep(1)
        self.page_get_number()
        sleep(1)
        self.page_check_record()
        sleep(1)
        self.page_click_submit()
        sleep(2)

    # 组装断言业务方法
    def page_assert_submit(self, text):
        # 修改数据状态为“审核通过”
        self.base_click(page.data_status)
        self.base_click(page.data_status_sxdsh)
        # 点击查询
        self.base_click(page.search_btn)
        # 获取问卷编号
        self.page_get_number()
        # 判断页面是否存在指定的问卷编号 并返回结果
        self.base_elem_is_exist()
