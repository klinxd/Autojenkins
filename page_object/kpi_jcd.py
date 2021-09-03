#KPI检测点配置页面
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class KpiJcd(BasePage):
    #新增检测点元素
    addElem = (By.XPATH,'//*[@id="app"]/div/section/section/main/div/div[1]/button[1]')
    #导入检测点元素
    importElem = (By.XPATH,'//*[@id="app"]/div/section/section/main/div/div[1]/button[2]')
    #导出检测点元素
    exportElem = (By.XPATH,'//*[@id="app"]/div/section/section/main/div/div[1]/button[3]')
    #编辑元素
    editElem = (By.XPATH,'//*[@id="app"]/div/section/section/main/div/div[2]/div[1]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[4]/div/div/span[1]')
    #删除元素
    deleteElem = (By.XPATH,'//*[@id="app"]/div/section/section/main/div/div[2]/div[1]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[4]/div/div/span[2]')

