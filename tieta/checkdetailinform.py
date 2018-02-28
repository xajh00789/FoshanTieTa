import time
import CommonSeleniumUtil
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from downloadpic import download_pic
import quanju_bianliang
from createdocument import create_document
import os
import shutil

#进入每一下载页面
def check_detail_inform(zhandian_bianma,driver):
    time.sleep(3)

    if quanju_bianliang.fault_happen==True:
        for radio in range(quanju_bianliang.radio_stop,20):
            WebDriverWait(driver, 20, 0.5).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[class="mini-grid-radio-mask"]')))

            options = driver.find_elements_by_xpath("//div[@class='mini-grid-radio-mask']")

            download_path=r'E:\迅雷下载\铁塔图片\临时图片3'
            if os.path.exists(download_path):
                shutil.rmtree(download_path)
            os.mkdir(download_path)

            options[radio].click()
            #  print("抄表记录查看")
            CommonSeleniumUtil.Clicks(driver, 'a[id="readingMeterBtn"] > span')
            quanju_bianliang.radio_stop = radio
            # 将打开的iframe关闭
            time.sleep(2)
            lujing=create_document(zhandian_bianma[radio])
            download_pic(driver,lujing)
            CommonSeleniumUtil.Clicks(driver, 'body > div[class="mini-panel mini-window mini-window-drag"] > div[class="mini-panel-border"] > div[class="mini-panel-header"] > div[class="mini-panel-header-inner"] > div[class="mini-tools"] > span:nth-child(4)')
            # download_path=r'C:\Users\xiaoxiong\Desktop\oracle\下载图片\下载图片\临时图片'
            # if os.path.exists(download_path):
            #     shutil.rmtree(download_path)
            # os.mkdir(download_path)
            time.sleep(2)
    else:
        for radio in range(0,20):
            #每次点击按钮关闭窗口之后页面会刷新，所有按钮要重新定位
            WebDriverWait(driver, 20, 0.5).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[class="mini-grid-radio-mask"]')))
            #time.sleep(2)
            options = driver.find_elements_by_xpath("//div[@class='mini-grid-radio-mask']")
            download_path=r'E:\迅雷下载\铁塔图片\临时图片3'
            if os.path.exists(download_path):
                shutil.rmtree(download_path)
            os.mkdir(download_path)
            options[radio].click()
          #  print("抄表记录查看")
            CommonSeleniumUtil.Clicks(driver,'a[id="readingMeterBtn"] > span')
            quanju_bianliang.radio_stop=radio
            time.sleep(2)
            lujing=create_document(zhandian_bianma[radio]) #根据站点编码创建文件夹
            download_pic(driver,lujing)
            CommonSeleniumUtil.Clicks(driver, 'body > div[class="mini-panel mini-window mini-window-drag"] > div[class="mini-panel-border"] > div[class="mini-panel-header"] > div[class="mini-panel-header-inner"] > div[class="mini-tools"] > span:nth-child(4)')
            # download_path=r'C:\Users\xiaoxiong\Desktop\oracle\下载图片\下载图片\临时图片'
            # if os.path.exists(download_path):
            #     shutil.rmtree(download_path)
            # os.mkdir(download_path)
            time.sleep(2)