#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@File   : .py
@Contact: ocewulf@126.com
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/2/22 17:44   ocewulf      1.0         None
"""
from selenium.webdriver.common.by import By

"""配置信息"""
# url地址
url = "http://10.1.93.111/ssohnDist/login"
"""
登录界面元素
"""
# 用户名
username = (By.CSS_SELECTOR, "input[placeholder='用户名']")
# 密码
pwd = (By.CSS_SELECTOR, "input[placeholder='密码']")
# # 验证码
# code = (By.ID, "validcode")
# 登录按钮
login_btn = (By.XPATH, "//*[@id='app']/div/div[1]/div[1]/div/div[2]/button/span")
# 登录名
login_name = (By.XPATH, "//*[@id='app']/div/div[2]/p")
"""
系统菜单界面元素
"""
# 系统主菜单栏
sys_menu_banner = (By.XPATH, "//*[@id='app']/div/div[3]/div/div")
# 二级菜单
second_menu_banner = (By.XPATH, "//*[@id='app']/div/div[5]/div[2]/div/div/div/ul/li/p")
"""
首页菜单栏元素
"""
data_info_menu = (By.XPATH, "//*[@id='app']/section/section/aside/div/ul/div[1]/li/div/p")
hotel_menu = (By.XPATH, "//*[@id='app']/section/section/aside/div/ul/div[1]/li/ul/li[1]/p")
"""
宾馆（酒店）主界面元素
"""
healthy_hazard_btn = (By.XPATH, "//*[@id='app']//span[text()=('健康危害因素调查管理')]")

"""
宾馆基本情况列表
"""
# 查询栏
data_status = (By.XPATH, "//*[@id='app']/section/section/main/div/div[1]/div/div[2]/div/div[1]/form/div[4]/div")
data_status_unsubmit = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]")
data_status_sxdsh = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]")
questionaire_id = (By.XPATH, "//*/div[@class='ez-input__inner'][6]")
search_btn = (By.XPATH, "//*/button/span[text()='查询'")
check_box = (By.XPATH, "//*[@id='app']/*/table/tbody/tr/td[1]/div/label/span/span")
# 列表页面
add_btn = (By.XPATH, "//span[text()='新增']")
edit_btn = (By.XPATH, ".//a/span[text()='编辑']")
del_btn = By.XPATH, ".//a/span[text()='删除']"
submit_btn = By.XPATH, "//span[text()='提交']"
confirm_btn = By.XPATH, "/html/body/div[2]/div/div[3]/button[2]/span"
table_rside = (By.XPATH, "//*[@id='app']/section/section/main/div/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div["
                         "5]/div[2]/table")
tr_list = (By.TAG_NAME, "tr")
td_list = (By.TAG_NAME, "td")
section = (By.XPATH, "//*[@id='app']/section")
table = (By.XPATH, "//*[@id='app']/section/section/main/div/div[1]/div/div[2]/div/div[2]/div[2]/div["
                   "1]/div/div[3]/table")
table_lside = (By.XPATH, "//*[@id='app']/section/section/main/div/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div["
                         "4]/div[2]/table")
questionaire_no = (By.XPATH, "/html/body/div[1]/section/section/main/div/div[1]/div/div[2]/div/div[2]/div[2]/div["
                             "1]/div/div[3]/table/tbody/tr/td[6]/div/div")

"""
宾馆（酒店）基本情况调查表新增页面
"""
# 表头信息
number = (By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[1]/div[1]/div/div/input")
investigate_start_time = (By.XPATH, "//input[@placeholder='选择时间'][1]")
rotation = (By.XPATH, "//input[@type='text' and @role='spinbutton'][1]")
# 一、基本情况
# 1.1 场所名称
place_name = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[1]/h4/div/input")
# 1.2 场所类别
hotel_type01 = (By.XPATH, "//span[text()='三星级以上（含三星级）宾馆']")
hotel_type02 = (By.XPATH, "//span[text()='三星级以下宾馆']")
hotel_type03 = (By.XPATH, "//span[text()='快捷酒店']")
# 1.3 场所地址
province = (By.XPATH, "//h4/div[@class='address-box']/div[1]/div/div/div[1]/input")
province_dropdown = (By.XPATH, "//ul/li/span[text()='海南省']")
city = (By.XPATH, "//h4/div[@class='address-box']/div[2]/div/div/div[1]/input")
city_dropdown = (By.XPATH, "/html/body/div[5]/div[1]/div[1]/ul")
# city_haikou = (By.XPATH, "//ul/li/span[text()='海口市']")
city_sanya = (By.XPATH, "/html/body/div[5]/div[1]/div[1]/ul/li[3]")
county = (By.XPATH, "//h4/div[@class='address-box']/div[3]/div/div/div[1]/input")
county_tianya = (By.XPATH, "//ul/li/span[text()='天涯区']")
addr_details = (By.XPATH, "//h4/div[@class='address-box']/div[4]/input")
# 1.4 有无卫生许可证
hygiene_license_yes = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[4]/div/label[2]")
hygiene_license_no = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[4]/div/label[1]")
# 1.5.1 开业年份
open_time = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[6]/h4/div/div/input")
# 1.5.2 经营客房面积、数量、日均客流量
room_area = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[7]/h4/div[1]/div/input")
room_num = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[7]/h4/div[2]/div/input")
daily_flow = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[7]/h4/div[3]/div/input")
# 1.5.3 从业人数、持续工作超过1年的人数
staff_total = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[8]/h4/div[1]/div/input")
staff_over_year = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[8]/h4/div[2]/div/input")
# 1.6 上一年度卫生监督量化分级管理等级评定情况？
ranking_no = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[9]/div/label[1]")
ranking_A = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[9]/div/label[2]")
ranking_B = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[9]/div/label[3]")
ranking_C = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[9]/div/label[4]")
# 1.7 本场所最近两年是否装修过?
decoration_no = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[10]/div/label[1]/span[2]")
decoration_yes = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[10]/div/label[2]/span[text()='是，请注明装修完成距今']")
decoration_time = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[10]/div/label[2]/span[2]/div/div/input")
# 1.7.1 装修程度
decoration_all = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[11]/div/label[1]")
decoration_partial = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[11]/div/label[2]")
# 1.8 宾馆客房临街一侧与道路的最短垂直距离：
vertical_distance_option1 = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[12]/div/label[1]")
vertical_distance_option2 = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[12]/div/label[2]")
vertical_distance_option3 = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[12]/div/label[3]")
vertical_distance_option4 = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[12]/div/label[4]")
vertical_distance_option5 = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[12]/div/label[5]")
# 1.9 客房门窗类型：
door_type_option1 = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[13]/div/label[1]")
door_type_option2 = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[13]/div/label[2]")
door_type_option3 = (By.XPATH, "//form/div[2]/div[1]/div[2]/div[13]/div/label[3]")
# 二、卫生管理状况
# 2.1 本场所是否建立卫生管理档案？
hygiene_archived_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[1]/div/label[2]")
hygiene_archived_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[1]/div/label[1]")
# 2.2.1 空气质量的检测情况：
air_detect_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[3]/div/label[1]")
air_detect_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[3]/div/label[1]")
# 2.2.2 微小气候（湿度、温度、风速）的检测情况：
climate_detect_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[4]/div/label[2]")
climate_detect_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[4]/div/label[1]")
# 2.2.3 饮用水质的检测情况：
water_detect_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[5]/div/label[2]")
water_detect_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[5]/div/label[1]")
# 2.2.4 照明的检测情况：
lighting_detect_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[6]/div/label[2]")
lighting_detect_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[6]/div/label[1]")
# 2.2.5 噪声的检测情况
noise_detect_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[7]/div/label[2]")
noise_detect_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[7]/div/label[1]")
# 2.2.6 顾客用品用具的清洗、消毒、更换情况
accessories_change_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[8]/div/label[2]")
accessories_change_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[8]/div/label[1]")
# 2.2.7 顾客用品用具的检测情况：
accessories_detect_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[9]/div/label[2]")
accessories_detect_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[9]/div/label[1]")
# 2.2.8 集中空调通风系统的清洗、消毒情况
aircon_detect_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[10]/div/label[2]")
aircon_detect_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[10]/div/label[1]")
# 2.2.9 集中空调通风系统的检测情况
ventilation_detect_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[11]/div/label[2]")
ventilation_detect_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[11]/div/label[1]")
# 2.2.10 空气、水质等指标的检测机构是
lab = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[12]/div/label[1]")
third_party_lab = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[12]/div/label[2]")
lab_own = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[12]/div/label[3]")
lab_other = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[12]/div/label[4]")
# 2.3 是否有专门的卫生管理人员？
sanitary_man_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[13]/div/label[2]")
sanitary_man_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[13]/div/label[1]")

# 2.3.1 卫生管理人员是专职或兼职？
sanitary_man_parttime = (By.XPATH, "/v/form/div[2]/div[2]/div[2]/div[14]/div/label[1]")
sanitary_man_fulltime = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[14]/div/label[2]")

# 2.4.1持健康证员工人数
clean_bill_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[16]/h4/div/div/input")
# 2.4.2是否每年组织员工健康体检？
healthy_check_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[17]/div/label[2]")
healthy_check_frequency = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[18]/h4/div/div/input")
healthy_check_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[17]/div/label[1]")
# 2.5.1有专门负责传染病防控的人员
disease_staff_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[20]/div/label[2]")
disease_staff_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[9]/div/label[1]")
# 2.5.2 建立疫情应急工作预案
epidemic_solution_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[21]/div/label[2]")
epidemic_solution_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[10]/div/label[1]")
# 2.5.3 建立员工健康监测制度
monitor_system_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[22]/div/label[2]")
monitor_system_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[11]/div/label[1]")
# 2.5.4 对员工进行传染病防护技能培训
disease_control_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[23]/div/label[2]")
disease_control_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[12]/div/label[1]")
# 2.5.5 复工或营业前进行预防性消毒
disinfect_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[24]/div/label[2]")
disinfect_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[13]/div/label[1]")
# 2.5.6 场所内洗手设施运行正常
facility_run_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[25]/div/label[2]")
facility_run_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[14]/div/label[1]")
# 2.5.7 设立疑似传染病人应急隔离区域
quarantine_area_yes = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[26]/div/label[2]")
quarantine_area_no = (By.XPATH, "//form/div[2]/div[2]/div[2]/div[15]/div/label[1]")
# 2.5.8 场所内是否配备下列物资？（可多选）
thermometer = (By.XPATH, "//span[text()='额温枪等测温设备']")
mask = (By.XPATH, "//span[text()='口罩']")
glove = (By.XPATH, "//span[text()='手套']")
soap = (By.XPATH, "//span[text()='洗手液/肥皂']")
dry_disinfectant = (By.XPATH, "//span[text()='速干手消毒剂']")
exposure_suit = (By.XPATH, "//span[text()='防护服']")
disinfectant = (By.XPATH, "//span[text()='消毒剂']")
dustbin = (By.XPATH, "//span[text()='废弃口罩专用垃圾桶']")
none = (By.XPATH, "//span[text()='以上均未配备']")
# 3.1 场所内是否使用集中空调通风系统？
airconditon_yes = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[1]/div/label[2]")
airconditon_no = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[1]/div/label[1]")
# 3.2 集中空调系统类别
airconditon_type1 = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[2]/div/label[1]")
airconditon_type2 = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[2]/div/label[2]")
airconditon_type3 = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[2]/div/label[3]")
# 3.3.1 关闭回风的应急装置
device1_yes = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[4]/div/label[2]")
device1_no = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[4]/div/label[1]")
# 3.3.2 关闭新风的应急装置
device2_yes = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[5]/div/label[2]")
device2_no = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[5]/div/label[1]")
# 3.3.3 控制空调系统分区域运行的装置：
area_control_yes = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[6]/div/label[2]")
area_control_no = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[6]/div/label[1]")
# 3.3.4 专用可开闭窗口或便于拆卸的风口
draught_yes = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[7]/div/label[2]")
draught_no = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[7]/div/label[1]")
# 3.3.5 空气净化消毒装置
airpurified_yes = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[8]/div/label[2]")
airpurified_no = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[8]/div/label[1]")
# 3.4 是否有开放式冷却塔
cooling_tower_yes = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[9]/div/label[2]")
cooling_tower_no = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[9]/div/label[1]")
# 3.4.1 今年冷却塔的运行时间
tower_run_time = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[10]/h4/div/div/input")
# 3.4.2-1 最近新风口距开放式冷却塔水平距离
tower_h_distance = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[11]/h4/div[1]/div/input")
# 3.4.2-2 最近新风口距开放式冷却塔垂直距离
tower_v_distance = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[11]/h4/div[2]/div/input")
# 3.4.3 开放式冷却塔周边30米内是否有人群聚集的固定场所？
assembly_no = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[12]/div/label[1]/span[2]")
assembly_carehome = (By.XPATH, "//span[text()='养老院']")
assembly_hospital = (By.XPATH, "//span[text()='医院']")
assembly_kindergarden = (By.XPATH, "//span[text()='幼儿园']")
assembly_other = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[12]/div/label[5]/span[2]']")
# 3.5 新风来自以下哪个位置？（多选）
air_from_room = (By.XPATH, "//span[text()='机房']")
air_from_stairway = (By.XPATH, "//span[text()='楼道']")
air_from_roof = (By.XPATH, "//span[text()='天棚吊顶']")
air_from_outside = (By.XPATH, "//span[text()='室外']")
air_from_other = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[13]/div/label[5]/span[2]")
air_other_text = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[13]/div/label[5]/span[2]/div/input")
# 3.5.1-1 新风口下缘距室外地坪垂直距离为
outside_h_distance = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[14]/h4/div[1]/div/input")
# 3.5.1-2 新风口下缘距排风垂直距离为
ventilate_distance = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[14]/h4/div[2]/div/input")
# 3.5.2 场所离垃圾站的距离？
less_20_meter = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[15]/div/label[1]")
twenty_to_fifty = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[15]/div/label[2]")
fifty_to_hundred = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[15]/div/label[3]")
hundred_to_2hundred = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[15]/div/label[4]")
more_2hundred = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[15]/div/label[5]")
# 3.6 空调机组是否设置初效过滤器？
aircon_filter_yes = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[16]/div/label[2]")
aircon_filter_no = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[16]/div/label[1]")
# 3.7 空调机组是否设置高效过滤器？
airconfilter2_yes = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[17]/div/label[2]")
aircon_filter2_no = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[17]/div/label[1]")
# 3.8 送风口和回风口是否设置防虫防鼠装置？
mothproof_yes = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[18]/div/label[2]")
mothproof_no = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[18]/div/label[1]")
# 3.9 空调系统采用以下哪种加湿方式？
humidify_no = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[19]/div/label[1]")
humidify_steam = (By.XPATH, "//span[text()='蒸汽加湿']")
humidify_by_mist = (By.XPATH, "//span[text()='自来水喷雾']")
humidify_by_water = (By.XPATH, "//span[text()='冷水蒸发']")
# 3.10 空调系统是否进行清洗？
aircondition_clean_no = (By.XPATH, "//span[text()='未清洗']")
aircondition_clean_yes = (By.XPATH, "//span[text()='已清洗(清洗频次']")
aircondition_clean_times = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[20]/div/label[2]/span[2]/div[1]/input")
aircondition_clean_date = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[20]/div/label[2]/span[2]/div[2]/input")
# 3.11 疫情常态化时期集中空调系统是如何运行的？（可多选）
aircondition_run_min = (By.XPATH, "//span[text()='将回风关至最小']")
aircondition_run_max = (By.XPATH, "//span[text()='以最大新风量运行']")
aircondition_run_off = (By.XPATH, "//span[text()='未开启']")
aircondition_run_on = (By.XPATH, "//span[text()='正常开启']")
aircondition_run_other = (By.XPATH, "//form/div[2]/div[3]/div[2]/div[21]/div/label[5]/span[2]")
# 4.1.1 被套、枕套（巾）、床单等卧具更换频率？
bed_change_no = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[2]/div/label[1]")
bed_change_customer = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[2]/div/label[2]")
bed_change_once = (By.XPATH, "//span[text()='一天一换'][1]")
bed_change_customer1 = (By.XPATH, "//span[text()='一客一换'][1]")
bed_change_other = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[2]/div/label[5]/span[2]")
# 4.1.2毛巾、脸巾、浴巾更换频率？
towel_change_no = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[3]/div/label[1]")
towel_change_customer = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[3]/div/label[2]")
towel_change_once = (By.XPATH, "//span[text()='一天一换'][2]")
towel_change_customer1 = (By.XPATH, "//span[text()='一客一换'][2]")
towel_change_other = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[3]/div/label[5]")
# 4.1.3 拖鞋更换频率？
slipper_change_no = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[4]/div/label[1]")
slipper_change_customer = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[4]/div/label[2]")
slipper_change_once = (By.XPATH, "//span[text()='一天一换'][3]")
slipper_change_customer1 = (By.XPATH, "//span[text()='一客一换'][3]")
slipper_change_other = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[4]/div/label[5]")
# 4.1.4洗漱用品更换频率？
toiletry_change_no = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[5]/div/label[1]")
toiletry_change_customer = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[5]/div/label[2]")
toiletry_change_once = (By.XPATH, "//span[text()='一天一换'][4]")
toiletry_change_customer1 = (By.XPATH, "//span[text()='一客一换'][4]")
toiletry_change_other = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[5]/div/label[5]")
# 4.2.1 电梯按钮是否消毒及频次：
button_clean_no = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[7]/div/label[1]")
button_clean_yes = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[7]/div/label[2]/span[1]/span")
button_clean_times = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[7]/div/label[2]/span[2]/div[1]/div/input")
button_clean_hour = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[7]/div/label[2]/span[2]/div[2]/div/input")
# 4.2.2 楼梯扶手是否消毒及频次：
handrail_clean_no = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[8]/div/label[1]")
handrail_clean_yes = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[8]/div/label[2]/span[1]/span")
handrail_clean_times = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[8]/div/label[2]/span[2]/div[1]/div/input")
handrail_clean_hour = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[8]/div/label[2]/span[2]/div[2]/div/input")
# 4.2.3 公共卫生间门把手是否消毒及频次：
doorknob_clean_no = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[9]/div/label[1]")
doorknob_clean_yes = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[9]/div/label[2]/span[1]/span")
doorknob_clean_times = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[9]/div/label[2]/span[2]/div[1]/div/input")
doorknob_clean_hour = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[9]/div/label[2]/span[2]/div[2]/div/input")
# 4.2.4 公共卫生间马桶按钮或把手是否消毒及频次：
closestool_clean_no = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[10]/div/label[1]")
closestool_clean_yes = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[10]/div/label[2]/span[1]/span")
closestool_clean_times = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[10]/div/label[2]/span[2]/div[1]/div/input")
closestool_clean_hour = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[10]/div/label[2]/span[2]/div[2]/div/input")
# 4.2.5 服务台是否消毒及频次：
counter_clean_no = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[11]/div/label[1]")
counter_clean_yes = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[11]/div/label[2]/span[1]/span")
counter_clean_times = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[11]/div/label[2]/span[2]/div[1]/div/input")
counter_clean_hour = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[11]/div/label[2]/span[2]/div[2]/div/input")
# 4.2.6 公共桌椅是否消毒及频次：
desk_clean_no = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[12]/div/label[1]")
desk_clean_yes = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[12]/div/label[2]/span[1]/span")
desk_clean_times = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[12]/div/label[2]/span[2]/div[1]/div/input")
desk_clean_hour = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[12]/div/label[2]/span[2]/div[2]/div/input")
# 4.2.7 客房内卫生间的洗漱池、浴盆是否消毒及频次：
bathroom_clean_no = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[13]/div/label[1]")
bathroom_clean_yes = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[14]/div/label[2]/span[1]/span")
bathroom_clean_times = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[13]/div/label[2]/span[2]/div[1]/div/input")
bathroom_clean_hour = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[13]/div/label[2]/span[2]/div[2]/div/input")
# 4.2.8 客房内卫生间的厕所或抽水马桶是否消毒及频次：
toilet_clean_no = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[14]/div/label[1]")
toilet_clean_yes = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[13]/div/label[2]/span[1]/span")
toilet_clean_times = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[14]/div/label[2]/span[2]/div[1]/div/input")
toilet_clean_hour = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[14]/div/label[2]/span[2]/div[2]/div/input")
# 4.3 卫生间清洗消毒的消毒剂类型？（可多选）
disinfect_type_84 = (By.XPATH, "//span[text()='84消毒液']")
disinfect_type_acid = (By.XPATH, "//span[text()='过氧乙酸消毒液']")
disinfect_type_powder = (By.XPATH, "//span[text()='漂白粉']")
disinfect_type_lysol = (By.XPATH, "//span[text()='来苏尔']")
disinfect_type_hydrogen = (By.XPATH, "//span[text()='双氧水']")
disinfect_type_other = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[15]/div/label[6]/span[1]/span")
type_other_text = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[15]/div/label[6]/span[2]/div/input")

# 4.4 是否有专门的消毒间？
disinfect_room_no = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[16]/div/label[1]")
disinfect_room_yes = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[16]/div/label[2]")
# 4.4.1 在消毒间内进行消毒的公共用品用具有哪些？(可多选)
tea_set = (By.XPATH, "//span[text()='茶具']")
tooth_glass = (By.XPATH, "//span[text()='漱口杯']")
bedding = (By.XPATH, "//span[text()='卧具（如床单、被罩、枕罩等）']")
towel = (By.XPATH, "//span[text()='毛巾、脸巾、浴巾']")
public_supply_other = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[17]/div/label[5]/span[2]")
# 4.4.2 在消毒间内采用的消毒方法是？(可多选)
boiling = (By.XPATH, "//span[text()='煮沸']")
disinfector = (By.XPATH, "//span[text()='消毒柜']")
soak = (By.XPATH, "//span[text()='浸泡']")
disinfect_way_other = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[18]/div/label[4]/span[2]")
# 4.5 员工工作服一般多久换洗一次？
times_day = (By.XPATH, "//span[text()='一天多次']")
once_day = (By.XPATH, "//span[text()='一天一次']")
once_2days = (By.XPATH, "//span[text()='两三天一次']")
once_4days = (By.XPATH, "//span[text()='三天以上']")
unknown = (By.XPATH, "//span[text()='不知道'][2]")
# 4.6 消毒工作是由谁具体做的？
staff = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[20]/div/label[1]")
company = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[20]/div/label[2]")
disinfector_other = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[20]/div/label[3]")
# 4.7 顾客用品用具是否由外单位清洗消毒？
clean_byoutsider_no = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[21]/div/label[1]")
clean_byoutsider_yes = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[21]/div/label[2]")
# 4.8 是否存在有顾客在场时消毒的情况？
customer_onsite_no = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[22]/div/label[1]")
customer_onsite_yes = (By.XPATH, "//form/div[2]/div[4]/div[2]/div[22]/div/label[2]")
# 5.1 场所内公共区域采用的通风换气方式？（可多选）
window_open = (By.XPATH, "//span[text()='开门开窗']")
aircondition = (By.XPATH, "//span[text()='集中空调通风系统']")
fresh_air = (By.XPATH, "//span[text()='新风系统']")
split_airconditon = (By.XPATH, "//span[text()='分体式空调']")
fan = (By.XPATH, "//span[text()='排风扇']")
ventilation_other = (By.XPATH, "//form/div[2]/div[5]/div[2]/div[1]/div/label[6]/span[2]")
ventilation_no = (By.XPATH, "//span[text()='无通风（跳到5.4）']")
# 5.2 场所内公共区域平均人为主动通风换气情况是？
ventilation_alltime = (By.XPATH, "//form/div[2]/div[5]/div[2]/div[2]/div/label[1]")
ventilation_average = (By.XPATH, "//form/div[2]/div[5]/div[2]/div[2]/div/label[2]/span[1]/span")
ventilation_freq = (By.XPATH, "//form/div[2]/div[5]/div[2]/div[2]/div/label[2]/span[2]/div/div/input")
# 5.3 场所内公共区域平均每次通风时长？
less_10m = (By.XPATH, "//span[text()='＜10分钟']")
ten_30m = (By.XPATH, "//span[text()='10～30分钟']")
thirty1_60m = (By.XPATH, "//span[text()='31～60分钟']")
more_60m = (By.XPATH, "//span[text()='＞60分钟']")
# 5.4 场所有专门的垃圾处理区域吗？
trash_dispose_yes = (By.XPATH, "//form/div[2]/div[5]/div[2]/div[4]/div/label[2]")
trash_dispose_no = (By.XPATH, "//form/div[2]/div[5]/div[2]/div[4]/div/label[1]")
# 5.5 场所内垃圾是否日产日清？
clean_day_yes = (By.XPATH, "//form/div[2]/div[5]/div[2]/div[5]/div/label[2]")
clean_day_no = (By.XPATH, "//form/div[2]/div[5]/div[2]/div[5]/div/label[1]")
# 5.6 客房卫生间洗手盆是否有水封？
water_seal_yes = (By.XPATH, "//form/div[2]/div[5]/div[2]/div[6]/div/label[2]")
water_seal_no = (By.XPATH, "//form/div[2]/div[5]/div[2]/div[6]/div/label[1]")
# 5.7  客房卫生间地漏是否有水封？
floor_drain_yes = (By.XPATH, "//form/div[2]/div[5]/div[2]/div[7]/div/label[2]")
floor_drain_no = (By.XPATH, "//form/div[2]/div[5]/div[2]/div[7]/div/label[1]")
# 5.8 公共卫生间每天打扫几次？
clean_times = (By.XPATH, "//form/div[2]/div[5]/div[2]/div[8]/h4/div/div/input")
# 调查结束时间
investigate_done_times = (By.XPATH, "//input[@placeholder='选择时间'][2]")
# 调查人
investigator = (By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[3]/div[2]/div/div[1]/input")
# 复核人
reviewer = (By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[3]/div[3]/div/div[1]/input")
# 填表日期
fill_date = (By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[3]/div[4]/div/div/input")
# 保存  关闭
save_button = (By.XPATH, "//span[text()='保存']")
close_button = (By.XPATH, "//span[text()='关闭']")
