#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/4/1 9:11 
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://10.1.93.111/ssohnDist/login")
driver.maximize_window()
sleep(3)
username = driver.find_element(By.CSS_SELECTOR, "input[placeholder='用户名']")
username.clear()
username.send_keys("hn_ggcs001")
pwd = driver.find_element(By.CSS_SELECTOR, "input[placeholder='密码']")
pwd.clear()
pwd.send_keys("Abcd1234")
sleep(3)
login_btn = driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div[1]/div/div[2]/button/span")
login_btn.click()
sleep(3)
sys_menu = driver.find_element(By.XPATH, "//*[@id='app']/div/div[3]/div/div")
sys_menu.click()
sleep(3)
sec_menu = driver.find_element(By.XPATH, "//*[@id='app']/div/div[5]/div[2]/div/div/div/ul/li/p")
sec_menu.click()
sleep(3)
curr_handle = driver.current_window_handle
all_handle = driver.window_handles
print(curr_handle.title())
driver.switch_to.window(all_handle[-1])
print(driver.current_url)

sleep(3)
data_info_menu = driver.find_element(By.XPATH, "//*[@id='app']/section/section/aside/div/ul/div[1]/li/div/p")
print(data_info_menu.text)
data_info_menu.click()

driver.find_element(By.XPATH, "//*[@id='app']/section/section/aside/div/ul/div[1]/li/ul/li[1]/p")