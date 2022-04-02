#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/4/2 9:11 
"""
from time import sleep

from base.base import Base
import page


# 封装新增方法-宾馆场所基本信息
class PageHotelBasicInfo(object):
    # 点击数据信息菜单进入二级菜单
    def page_click_menubar(self):
        self.base_click(page.data_info_menu)
        sleep(1)
        self.base_click(page.hotel_menu)

    # 点击健康危害因素调查管理按钮进入宾馆基本情况调查表界面
    def page_click_hazard_btn(self):
        pass

    # 点击新增，打开调查表填报界面
    def page_click_new(self):
        pass

    # 填报调查表
    def page_fill_questionnaire(self):
        pass

    # 点击保存
    def page_save_questionnaire(self):
        pass