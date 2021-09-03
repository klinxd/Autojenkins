#基础工具类，封装各个页面公共都需要的关键词驱动
from selenium import webdriver

class BasePage:

     def __init__(self,driver):
        self.driver = driver

     #定位元素
     def findElem(self,elem):
         return self.driver.find_element(*elem)

     #输入框输入值
     def input(self,elem,text):
         self.findElem(elem).send_keys(text)

    #单击按钮
     def click(self,elem):
         self.findElem(elem).click()