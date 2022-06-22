#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/5/13 14:38 
"""
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver


class TestDelHotBasicInfo:
    # 初始化操作（打开浏览器及环境地址并登录）
    def setup_class(self):
        driver = GetDriver.get_web_driver(page.url)
        # 获取PageIn对象
        self.page_in = PageIn(driver)
        # 通过PageIn对象调用登录（成功）方法
        self.page_in.page_get_page_login().page_login_success()
        # 获取PageSysMenu对象并调用点击菜单方法进入首页
        self.menu = self.page_in.page_get_page_sysmenu()
        # 实例化PageDelBasicHotInfo对象
        self.del_hotel_info = self.page_in.page_get_page_del_hotel_info()

    # def teardown_class(self):
    #     # 关闭driver
    #     GetDriver().quit_web_driver()

    def test_del_hot_info(self, target_id):
        # 调用PageSysMenu对象的page_sys_menu业务组合方法进入宾馆主界面
        self.menu.page_sys_menu()
        # 调用page_del_basic_hotel_info业务组合方法删除调查表记录
        self.del_hotel_info.page_del_basic_hotel_info(target_id)
        # 界面断言：验证列表是否存在指定问卷编号的记录
        self.submit.page_assert_submit()
