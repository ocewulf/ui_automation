#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/4/2 9:11 
"""
from time import sleep

from selenium.webdriver import ActionChains

from base.base import Base
import page


# 封装新增方法-宾馆场所基本信息
class PageNewHotelBasicInfo(Base):
    # 点击数据信息菜单进入二级菜单
    def page_click_menubar(self):
        self.base_click(page.data_info_menu)
        # 点击宾馆菜单进入宾馆界面
        self.base_click(page.hotel_menu)

    # 点击健康危害因素调查管理按钮进入宾馆基本情况调查表界面
    def page_click_hazard_btn(self):
        self.base_click(page.healthy_hazard_btn)

    # 点击新增，打开调查表填报界面
    def page_click_new(self):
        self.base_click(page.add_btn)

    # 填报调查表
    def page_fill_header(self, id, batch):
        # 表头
        self.base_input(page.number, id)
        # start_time = self.base_find(page.investigate_start_time).clear()
        # start_time.send_keys("11:00:00")
        self.base_input(page.rotation, batch)

    # 一 基础情况
    def page_fill_basic(self, place, address, opentime, roomarea, roomnum, flow, staffs, staff_one_year, decro_time):
        place = self.base_input(page.place_name, place)

        self.base_click(page.hotel_type01)
        self.base_click(page.province)
        self.base_click(page.province_dropdown)

        self.base_click(page.city)
        # ActionChains(self.driver).move_to_element(self.base_find(page.city_dropdown)).perform()
        self.base_click(page.city_sanya)

        self.base_click(page.county)
        self.base_click(page.county_tianya)

        self.base_input(page.addr_details, address)

        self.base_click(page.hygiene_license_yes)
        self.base_input(page.open_time, opentime)

        self.base_input(page.room_area, roomarea)

        self.base_input(page.room_num, roomnum)

        self.base_input(page.daily_flow, flow)

        self.base_input(page.staff_total, staffs)

        self.base_input(page.staff_over_year, staff_one_year)

        self.base_click(page.ranking_A)
        self.base_click(page.decoration_yes)

        self.base_input(page.decoration_time, decro_time)

        self.base_click(page.decoration_partial)
        self.base_click(page.vertical_distance_option3)
        self.base_click(page.door_type_option2)

    # 二 卫生管理状况
    def page_fill_healty(self, bill_no, healthy_check):
        self.base_click(page.hygiene_archived_yes)
        self.base_click(page.air_detect_yes)
        self.base_click(page.climate_detect_yes)
        self.base_click(page.water_detect_yes)
        self.base_click(page.lighting_detect_yes)
        self.base_click(page.noise_detect_yes)
        self.base_click(page.accessories_change_yes)
        self.base_click(page.accessories_detect_yes)
        self.base_click(page.aircon_detect_yes)
        self.base_click(page.ventilation_detect_yes)
        self.base_click(page.lab)
        self.base_click(page.sanitary_man_yes)
        self.base_click(page.sanitary_man_fulltime)

        self.base_input(page.clean_bill_no, bill_no)

        self.base_click(page.healthy_check_yes)
        self.base_input(page.healthy_check_frequency, healthy_check)

        self.base_click(page.disease_staff_yes)
        self.base_click(page.epidemic_solution_yes)
        self.base_click(page.monitor_system_yes)
        self.base_click(page.disease_control_yes)
        self.base_click(page.disinfect_yes)
        self.base_click(page.facility_run_yes)
        self.base_click(page.quarantine_area_yes)
        self.base_click(page.thermometer)
        self.base_click(page.mask)
        self.base_click(page.glove)
        self.base_click(page.soap)
        self.base_click(page.dry_disinfectant)
        self.base_click(page.exposure_suit)

    # 三 集中空调卫生状况
    def page_fill_aircondition(self, tow_run_time, tow_h_distance, tow_v_distance, outside_distance, ventil_distance,
                               aircon_clean_times, aircon_clean_date):
        self.base_click(page.airconditon_yes)
        self.base_click(page.airconditon_type1)
        self.base_click(page.device1_yes)
        self.base_click(page.device2_yes)
        self.base_click(page.area_control_yes)
        self.base_click(page.draught_yes)
        self.base_click(page.airpurified_yes)
        self.base_click(page.cooling_tower_yes)
        self.base_input(page.tower_run_time, tow_run_time)

        self.base_input(page.tower_h_distance, tow_h_distance)

        self.base_input(page.tower_v_distance, tow_v_distance)

        self.base_click(page.assembly_no)
        self.base_click(page.air_from_room)
        self.base_click(page.air_from_stairway)
        self.base_click(page.air_from_roof)
        self.base_input(page.outside_h_distance, outside_distance)

        self.base_input(page.ventilate_distance, ventil_distance)

        self.base_click(page.more_2hundred)
        self.base_click(page.aircon_filter_yes)
        self.base_click(page.airconfilter2_yes)
        self.base_click(page.mothproof_yes)
        self.base_click(page.humidify_steam)

        self.base_click(page.aircondition_clean_yes)
        self.base_input(page.aircondition_clean_times, aircon_clean_times)

        self.base_input(page.aircondition_clean_date, aircon_clean_date)

        self.base_click(page.aircondition_run_min)

    # 四、常态化情景下卫生消毒情况
    def page_fill_disinfectants(self, but_clean_t, but_clean_h, handr_clean_t, handr_clean_h, door_clean_t,
                                door_clean_h, close_clean_t, close_clean_h, counter_clean_t, counter_clean_h,
                                desk_clean_t, desk_clean_h, bathroom_clean_t, bathroom_clean_h, toilet_clean_t,
                                toilet_clean_h):
        self.base_click(page.bed_change_customer)
        self.base_click(page.towel_change_customer)
        self.base_click(page.slipper_change_customer)
        self.base_click(page.toiletry_change_customer)
        self.base_click(page.button_clean_yes)

        self.base_input(page.button_clean_times, but_clean_t)

        self.base_input(page.button_clean_hour, but_clean_h)

        self.base_click(page.handrail_clean_yes)
        self.base_input(page.handrail_clean_times, handr_clean_t)

        self.base_input(page.handrail_clean_hour, handr_clean_h)

        self.base_click(page.doorknob_clean_yes)
        self.base_input(page.doorknob_clean_times, door_clean_t)

        self.base_input(page.doorknob_clean_hour, door_clean_h)

        self.base_click(page.closestool_clean_yes)
        self.base_input(page.closestool_clean_times, close_clean_t)

        self.base_input(page.closestool_clean_hour, close_clean_h)

        self.base_click(page.counter_clean_yes)
        self.base_input(page.counter_clean_times, counter_clean_t)

        self.base_input(page.counter_clean_hour, counter_clean_h)

        self.base_click(page.desk_clean_yes)
        self.base_input(page.desk_clean_times, desk_clean_t)

        self.base_input(page.desk_clean_hour, desk_clean_h)

        self.base_click(page.bathroom_clean_yes)
        self.base_input(page.bathroom_clean_times, bathroom_clean_t)
        self.base_input(page.bathroom_clean_hour, bathroom_clean_h)

        self.base_click(page.toilet_clean_yes)
        self.base_input(page.toilet_clean_times, toilet_clean_t)

        self.base_input(page.toilet_clean_hour, toilet_clean_h)

        self.base_click(page.disinfect_type_84)
        self.base_click(page.disinfect_type_acid)
        self.base_click(page.disinfect_type_powder)

        self.base_click(page.disinfect_room_yes)
        self.base_click(page.tea_set)
        self.base_click(page.tooth_glass)
        self.base_click(page.bedding)
        self.base_click(page.towel)

        self.base_click(page.boiling)
        self.base_click(page.disinfector)
        self.base_click(page.soak)

        self.base_click(page.once_day)

        self.base_click(page.staff)

        self.base_click(page.clean_byoutsider_yes)

        self.base_click(page.customer_onsite_yes)

    # 五、常态化情景下环境卫生状况
    def page_fill_environment(self, clean_t):
        self.base_click(page.window_open)
        self.base_click(page.fresh_air)
        self.base_click(page.fan)

        self.base_click(page.ventilation_alltime)

        self.base_click(page.more_60m)

        self.base_click(page.trash_dispose_yes)

        self.base_click(page.clean_day_yes)

        self.base_click(page.water_seal_yes)

        self.base_click(page.floor_drain_yes)

        self.base_input(page.clean_times, clean_t)

    # 表尾
    def page_fill_tail(self, investigate, review, input_date):
        # end_time = self.base_find(page.investigate_done_times)
        # end_time.clear()
        # end_time.send_keys("12:00:00")

        self.base_input(page.investigator, investigate)

        self.base_input(page.reviewer, review)

        self.base_input(page.fill_date, input_date)

    # 点击保存，保存调查表
    def page_save(self):
        self.base_click(page.save_button)

    # 获取问卷编号
    def page_get_survy_no(self, id):
        tds = self.base_find_elements(page.td_list)
        for td in tds:
            text = td.text
            if text == id:
                return text

        # 组合业务方法
    def page_complete_survey(self, id, batch, place, address, opentime, roomarea, roomnum, flow, staffs,
                             staff_one_year, decro_time, bill_no, healthy_check, tow_run_time, tow_h_distance,
                             tow_v_distance, outside_distance, ventil_distance, aircon_clean_times, aircon_clean_date,
                             but_clean_t, but_clean_h, handr_clean_t, handr_clean_h, door_clean_t, door_clean_h,
                             close_clean_t, close_clean_h, counter_clean_t, counter_clean_h,desk_clean_t, desk_clean_h,
                             bathroom_clean_t, bathroom_clean_h, toilet_clean_t, toilet_clean_h, clean_t, investigate,
                             review, input_date, expected):
        # 点击菜单栏菜单，进入宾馆（酒店）主页
        sleep(1)
        self.page_click_menubar()
        # 点击健康危害因素管理按钮进入宾馆基本情况表界面
        sleep(1)
        self.page_click_hazard_btn()
        # 点击新增按钮，打开调查表新增界面
        sleep(1)
        self.page_click_new()
        # 填写调查表
        self.page_fill_header(id, batch)
        self.page_fill_basic(place, address, opentime, roomarea, roomnum, flow, staffs, staff_one_year, decro_time)
        self.page_fill_healty(bill_no, healthy_check)
        self.page_fill_aircondition(tow_run_time, tow_h_distance, tow_v_distance, outside_distance, ventil_distance,
                               aircon_clean_times, aircon_clean_date)
        self.page_fill_disinfectants(but_clean_t, but_clean_h, handr_clean_t, handr_clean_h, door_clean_t,
                                door_clean_h, close_clean_t, close_clean_h, counter_clean_t, counter_clean_h,
                                desk_clean_t, desk_clean_h, bathroom_clean_t, bathroom_clean_h, toilet_clean_t,
                                toilet_clean_h)
        self.page_fill_environment(clean_t)
        self.page_fill_tail(investigate, review, input_date)

        # 点击保存按钮，提交调查表
        self.page_save()
