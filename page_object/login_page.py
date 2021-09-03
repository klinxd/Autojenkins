#登录页面对象类
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from base.base_page import BasePage

class LoginPage(BasePage):

    #登录页面url
    url = "https://test.web.moedu.net/login/#/login"
    user = (By.CSS_SELECTOR,'[type="text"]')
    pwd = (By.CSS_SELECTOR,'[type="password"]')
    loginButton = (By.XPATH,'//*[@id="logincontent"]/div[2]/div/div/div/div[2]/button')

    #登录操作
    def login(self,user,passwd):
        self.driver.get(self.url)
        time.sleep(2)
        self.input(self.user,user)
        time.sleep(2)
        self.input(self.pwd,passwd)
        time.sleep(2)
        self.click(self.loginButton)
        time.sleep(2)
