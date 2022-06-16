#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/4/22 13:57 
"""
from time import sleep

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
import pytest

from tools.get_log import GetLogger
from tools.read_db import ReadDB
from tools.read_file import read_file

log = GetLogger.get_log()


class TestNewHotelBasicInfo:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver().get_web_driver(page.url)
        # 获取统一入口类PageIn，调用登录方法进行登录
        self.page_in = PageIn(driver)
        self.page_in.page_get_page_login().page_login_success()
        # 获取PageSysMenu对象，并调用page_sys_menu方法进入主界面
        sleep(3)
        self.menu = self.page_in.page_get_page_sysmenu()
        sleep(3)
        self.survey = self.page_in.page_get_page_new_hotel_info()

    # 结束
    # def teardown_class(self):
    #     GetDriver().quit_web_driver()

    # 调查表填写
    input_value = (
        "id, batch, place, address, opentime, roomarea, roomnum, flow, staffs,staff_one_year, decro_time,bill_no, "
        "healthy_check, tow_run_time, tow_h_distance, tow_v_distance, outside_distance, ventil_distance, "
        "aircon_clean_times, aircon_clean_date, but_clean_t, but_clean_h, handr_clean_t,handr_clean_h, door_clean_t, "
        "door_clean_h, close_clean_t, close_clean_h, counter_clean_t, counter_clean_h, desk_clean_t, desk_clean_h, "
        "bathroom_clean_t, bathroom_clean_h, toilet_clean_t, toilet_clean_h, clean_t, investigate, review, "
        "input_date, expected")

    @pytest.mark.parametrize(input_value, read_file("hotel_new_basic_info.yaml"))
    @pytest.mark.run(order=3)
    def test_hotel_basic_info(self, id, batch, place, address, opentime, roomarea, roomnum, flow, staffs,
                              staff_one_year, decro_time,
                              bill_no, healthy_check, tow_run_time, tow_h_distance, tow_v_distance, outside_distance,
                              ventil_distance,
                              aircon_clean_times, aircon_clean_date, but_clean_t, but_clean_h, handr_clean_t,
                              handr_clean_h, door_clean_t,
                              door_clean_h, close_clean_t, close_clean_h, counter_clean_t, counter_clean_h,
                              desk_clean_t, desk_clean_h,
                              bathroom_clean_t, bathroom_clean_h, toilet_clean_t, toilet_clean_h, clean_t, investigate,
                              review, input_date, expected):
        # 打开系统主界面并点击菜单栏菜单
        self.menu.page_sys_menu()

        self.survey.page_complete_survey(id, batch, place, address, opentime, roomarea, roomnum, flow, staffs,
                                         staff_one_year, decro_time,
                                         bill_no, healthy_check, tow_run_time, tow_h_distance, tow_v_distance,
                                         outside_distance,
                                         ventil_distance,
                                         aircon_clean_times, aircon_clean_date, but_clean_t, but_clean_h, handr_clean_t,
                                         handr_clean_h, door_clean_t,
                                         door_clean_h, close_clean_t, close_clean_h, counter_clean_t, counter_clean_h,
                                         desk_clean_t, desk_clean_h,
                                         bathroom_clean_t, bathroom_clean_h, toilet_clean_t, toilet_clean_h, clean_t,
                                         investigate,
                                         review, input_date, expected)

        sleep(2)
        # 数据库断言新增调查表记录
        sql = "select code from T_BASE_INFO_HOTEL where BASE_PLACE_NAME = '%s'" % place
        result = ReadDB().get_sql_one(sql)
        print("数据库查询的记录是:", result)
        assert result[0] == id
        print("\n 数据库返回的问卷编号与界面新增录入时的编号一致，问卷编号为{}".format(result[0]))
        # 界面断言
        try:
            assert expected == self.survey.page_get_survy_no(id)
            print("期望问卷编号值与实际界面记录显示的问卷编号值一致，测试通过")
        except Exception as e:
            log.error("验证失败，错误信息：{}".format(e))
            # 输出错误信息
            print("错误信息：", e)
            # 截图
            self.survey.base_get_img()
            # 抛出异常
            raise
