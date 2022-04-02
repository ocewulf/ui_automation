from selenium import webdriver
from aip import AipOcr
from time import sleep
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class LoginCase(unittest.TestCase):
    # 初始化并打开chrome
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        sleep(3)

    def login(self, username, password, vcode):
        self.driver.get("http://10.241.99.11:8999/uauth/web/Login.html")
        for i in range(3):
            self.driver.refresh()
            sleep(5)
        user = self.driver.find_element_by_id('accountCode')
        user.clear()
        user.send_keys(username)

        pwd = self.driver.find_element_by_id('passward')
        pwd.clear()
        pwd.send_keys(password)

        valcode = self.driver.find_element_by_id('validcode')
        valcode.clear()
        valcode.send_keys(vcode)

        signbtn = self.driver.find_element_by_id('signInBtn')
        signbtn.click()
        sleep(5)

        for i in range(3):
            self.driver.refresh()
            sleep(5)

    # 测试登录
    def test_login_ok(self):
        # 验证码识别
        self.driver.get("http://10.241.99.11:8999/uauth/web/Login.html")
        for i in range(4):
            self.driver.refresh()
            sleep(5)
        client = AipOcr('25613421', '4clUXNAwEGlCQ77Ob6DfBEWA', 'VMxLp3UoGwhQeb2s9obuGvCWsxGeyK5S')
        captcha = self.driver.find_element_by_xpath('//*[@id="img"]')
        screenshot = captcha.screenshot_as_png

        code = client.basicGeneral(screenshot, {})
        print(code)

        firstval = list(code.values())[0]
        print(firstval)
        dic = firstval[0]
        word = list(dic.values())[0]

        # 用户名、密码、验证码正确
        self.login('admin', 'Admin@123', word)
        sleep(3)
        element = self.driver.find_element_by_id('userHello')
        self.assertIn('超***员' in element.text)
        self.driver.get_screenshot_as_file("E:\login_ok.jpg")

    def tearDown(self):
        sleep(2)
        print('测试完成')


if __name__ == '__main__':
    unittest.main()
