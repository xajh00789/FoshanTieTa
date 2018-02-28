#coding:utf8
# uncompyle6 version 2.14.3
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: D:\cppy\code\CommonSeleniumUtil.py
# Compiled at: 2017-09-11 12:48:08
# Size of source mod 2**32: 2601 bytes
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#点击
def Clicks(driver, Brands, time_s=20):
    time.sleep(0.5)
    element = WebDriverWait(driver, time_s, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, Brands)))
    element.click()

#键盘多按键操作1
def keyboardAction(driver,Brands,word,time_s=60):
    time.sleep(0.5)
    WebDriverWait(driver, time_s, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, Brands)))
    driver.find_element_by_css_selector(Brands).send_keys(Keys.CONTROL,word)

#键盘删除操作
def keyboardAction_BACKSPACE(driver,Brands,time_s=60):
    time.sleep(0.5)
    WebDriverWait(driver, time_s, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, Brands)))
    driver.find_element_by_css_selector(Brands).send_keys(Keys.BACKSPACE)

#键盘回车操作
def keyboardAction_ENTER(driver,Brands,time_s=60):
    time.sleep(0.5)
    WebDriverWait(driver, time_s, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, Brands)))
    driver.find_element_by_css_selector(Brands).send_keys(Keys.ENTER)


#获取返回元素属性
def shuxingAcquisition(driver,Brands,shuxing,time_s=60):
    time.sleep(0.5)
    WebDriverWait(driver, time_s, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, Brands)))
    shuxing_text = driver.find_element_by_css_selector(Brands).get_attribute(shuxing)
    return shuxing_text

#输入
def TypeIns(driver, Brands, contants, time_s=60):
    time.sleep(0.5)
    element = WebDriverWait(driver, time_s, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, Brands)))
    element.clear()
    time.sleep(0.5)
    element.send_keys(contants)



def TheDropDownChoices(driver, Brands, contants, time_s=60):
    time.sleep(0.5)
    element = WebDriverWait(driver, time_s, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, Brands)))
    element.select_by_visible_text(contants)


def TheDropDownChoicesIndex(driver, Brands, index, time_s=60):
    time.sleep(0.5)
    element = WebDriverWait(driver, time_s, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, Brands)))
    element.select_by_index(index)


def Hoverings(driver, Brands, time_s=20):
    time.sleep(1)
    element = WebDriverWait(driver, time_s, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, Brands)))
    ActionChains(driver).move_to_element(element).perform()

#定位获取text文本
def InformationAcquisition(driver, Brands, time_s=60):
    time.sleep(0.5)
    element = WebDriverWait(driver, time_s, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, Brands)))
    return element.text

#定位获取text文本
def InformationAcquisitions(driver, Brands, time_s=60):
    """��ȡ���ݺ���,����Ԫ�ص�CSS"""
    time.sleep(0.5)
    element = WebDriverWait(driver, time_s, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, Brands)))
    return element.text


#定位iframe并进入框架
def IframeCss(driver, Brands, time_s=20):
    """��ȡiframe,����Ԫ�ص�CSS"""
    time.sleep(0.5)
    WebDriverWait(driver, time_s, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, Brands)))
    driver.switch_to.frame(driver.find_element_by_css_selector(Brands))
# okay decompiling CommonSeleniumUtil.pyc
