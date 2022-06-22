#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/5/7 23:00 
"""
from time import sleep

import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.read_db import ReadDB
from tools.read_file import read_file


class TestModifyHotelBasicInfo:
    def setup_class(self):
        # 初始化driver
        driver = GetDriver().get_web_driver(page.url)
        # 获取统一入口类对象Pagin
        self.pagein = PageIn(driver)
        # 获取PageLogin对象并登录
        self.pagein.page_get_page_login().page_login_success()
        # 获取PageSysMenu对象进入主界面
        self.menu = self.pagein.page_get_page_sysmenu()
        # 获取PageModifyHotelBasicInfo
        self.page_del = self.pagein.page_get_page_mod_hotel_info()

    # def teardown_class(self):
    #     # 关闭driver
    #     GetDriver().quit_web_driver()

    value = (
        "id, batch, place, address, opentime, roomarea, roomnum, flow, staffs,staff_one_year, decro_time,bill_no, "
        "healthy_check, tow_run_time, tow_h_distance, tow_v_distance, outside_distance, ventil_distance, "
        "aircon_clean_times, aircon_clean_date, but_clean_t, but_clean_h, handr_clean_t,handr_clean_h, door_clean_t, "
        "door_clean_h, close_clean_t, close_clean_h, counter_clean_t, counter_clean_h, desk_clean_t, desk_clean_h, "
        "bathroom_clean_t, bathroom_clean_h, toilet_clean_t, toilet_clean_h, clean_t, investigate, review, "
        "input_date, expected, orgin_id")

    @pytest.mark.parametrize(value, read_file("hotel_mod_basic_info.yaml"))
    @pytest.mark.run(order=4)
    def test_modify_hotel_basic_info(self, id, batch, place, address, opentime, roomarea, roomnum, flow, staffs,
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
                                     review, input_date, expected, orgin_id):
        # 调用PageSysMenu对象的page_sys_menu业务组合方法进入宾馆主界面
        self.menu.page_sys_menu()
        # 调用PageModifyHotelBasicInfo的page_modify_survey进入修改界面修改信息
        self.pagemodinfo.page_modify_survey(id, batch, place, address, opentime, roomarea, roomnum, flow, staffs,
                                            staff_one_year, decro_time,
                                            bill_no, healthy_check, tow_run_time, tow_h_distance, tow_v_distance,
                                            outside_distance,
                                            ventil_distance,
                                            aircon_clean_times, aircon_clean_date, but_clean_t, but_clean_h,
                                            handr_clean_t,
                                            handr_clean_h, door_clean_t,
                                            door_clean_h, close_clean_t, close_clean_h, counter_clean_t,
                                            counter_clean_h,
                                            desk_clean_t, desk_clean_h,
                                            bathroom_clean_t, bathroom_clean_h, toilet_clean_t, toilet_clean_h, clean_t,
                                            investigate,
                                            review, input_date, expected, orgin_id)

        sleep(2)

        # 数据库断言
        sql = "select code from T_BASE_INFO_HOTEL where base_place_name = '%s'" % place
        result = ReadDB().get_sql_one(sql)
        print("数据库查询的记录是:", result)
        assert result[0] == id
        print("\n 数据库返回的问卷编号与界面新增录入时的编号一致，问卷编号为{}".format(result[0]))
        # 界面断言
        assert expected == self.pagemodinfo.page_get_survy_no(id)
        print("期望问卷编号值与实际界面记录显示的问卷编号值一致，测试通过")
