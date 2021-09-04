# 对登录页面进行单元测试
# 对登录页面进行单元测试
import time
import unittest
from selenium import webdriver
from login_page import LoginPage
from ddt import ddt,data,unpack,file_data


@ddt
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.lg = LoginPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    @file_data('uer.yaml')
    def test_1(self,**uer):
        user = uer.get('name')
        pwd = uer.get('pwd')
        self.lg.login(user, pwd)
        time.sleep(2)

    # def test_2(self):
    #     self.lg.login('hd_admin', '000000a')
    #     time.sleep(2)


if __name__ == '__main__':
    unittest.main()
