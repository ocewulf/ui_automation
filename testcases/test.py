#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/5/11 17:06 
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.execute_script()


js = "var q=document.getElementsByClassName('table-content')[0].scrollTop=1000"
