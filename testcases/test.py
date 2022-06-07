#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/5/11 17:06 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()
# driver.execute_script()
#
#
# js = "var q=document.getElementsByClassName('table-content')[0].scrollTop=1000"
#
# row = driver.find_elements_by_tag_name("tr")
# list = []
# for i in row:
#     j = i.find_elements_by_tag_name()
# #
# table = driver.find_element(By.XPATH, "")
# table.find_elements(By.TAG_NAME, )
list = [['海南省', '三亚市', '天涯区', '2021-12-08', '1', 'GGCS-BASICINFO-004', '未提交'], ['海南省', '海口市', '市辖区', '2021-12-31', '1', 'Anson01', '未提交'], ['海南省', '海口市', '龙华区', '2021-12-03', '1', 'Anson011', '未提交'], ['海南省', '海口市', '秀英区', '2021-12-06', '2', 'Anson0061', '未提交'], ['海南省', '三亚市', '天涯区', '2022-01-18', '1', 'HOTEL2022', '未提交'], ['海南省', '三亚市', '天涯区', '2022-05-17', '1', '2022051701', '未提交']]
print(list[5][5].strip())

