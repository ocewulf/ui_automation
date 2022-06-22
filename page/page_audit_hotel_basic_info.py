#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/6/22 10:04 
"""
from time import sleep

import page
from base.base import Base


class PageAuditHotelBasicInfo(Base):
    # 第一步：登录系统
    # 第二步：点击滑动菜单窗口进入首页
    # 第三步：点击菜单栏数据信息-宾馆（酒店），打开宾馆主界面
    def page_click_menubar(self):
        self.base_click(page.data_info_menu)
        self.base_click(page.hotel_menu)

    # 第四步：点击健康危害因素调查管理按钮
    def page_click_harzard(self):
        self.base_click(page.healthy_hazard_btn)

    # 第五步：输入要审批的监测问卷编号
    def page_input_id(self, input_id):
        self.base_input(page.query_id, input_id)

    # 第六步：点击查询
    def page_click_query(self):
        self.base_click(page.search_btn)

    # 第七步：勾选记录
    def page_check_record(self):
        self.base_click(page.check_box)

    # 第八步：点击审批同意
    def page_click_audit_btn(self):
        self.base_click(page.agreed_btn)

    # 组合业务方法
    def page_audit_hotel_basic(self, input_id):
        sleep(2)
        self.page_click_menubar()
        sleep(2)
        self.page_click_harzard()
        sleep(2)
        self.page_input_id(input_id)
        sleep(1)
        self.page_click_query()
        sleep(2)
        self.page_check_record()
        sleep(1)
        self.page_click_audit_btn()
        sleep(2)
