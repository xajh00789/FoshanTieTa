import CommonSeleniumUtil
import time
from selenium.common.exceptions import TimeoutException
import quanju_bianliang
from selenium import webdriver
from movePhoto import move_Photo
from check_download import check_whether_all_download
import os

def download_pic(driver,lujing):

    CommonSeleniumUtil.IframeCss(driver,'div[class="mini-panel-body"] > iframe')
    while(True):

        options= driver.find_elements_by_xpath('//a[contains(text(),"下载")]')
        whether_next = driver.find_element_by_css_selector('a[id="mini-14"]').get_attribute("class")
        if options!=[]:
            try:
                count = len(options)

                for i in range(0, count):
                    options[i].click()
                time.sleep(2)

                #check_whether_all_download()
                unDownload_exist = True
                while (unDownload_exist == True):
                    unDownload_exist = False
                    for filename in os.listdir('E:\迅雷下载\铁塔图片\临时图片3\\'):
                        if os.path.splitext(filename)[1] == '.crdownload':
                            print(filename)
                            unDownload_exist = True
                    time.sleep(1)

                whether_exist=os.path.exists(r'E:\迅雷下载\铁塔图片\临时图片3')
                while(whether_exist):
                    move_Photo(lujing)
            #    time.sleep(5)
            except Exception as e:
               # print(e)
                error1='Message: stale element reference: element is not attached to the page document'
                if error1 in str(e):
                    whether_exist=os.path.exists(r'E:\迅雷下载\铁塔图片\临时图片3')
                    while(whether_exist):
                         time.sleep(2)
                         move_Photo(lujing)
                         time.sleep(2)
                         break
                quanju_bianliang.accident=1
        if quanju_bianliang.accident==1:
            quanju_bianliang.accident=0
            break
        if whether_next!="mini-button mini-button-plain mini-button-disabled":
            quanju_bianliang.accident = 0
            try:
                CommonSeleniumUtil.Clicks(driver, 'a[id="mini-14"] > span')
                time.sleep(2)
            except Exception as e:
                error1 = 'Message: stale element reference: element is not attached to the page document'
                if error1 in str(e):
                    whether_exist = os.path.exists(r'E:\迅雷下载\铁塔图片\临时图片3')
                    while (whether_exist):
                        time.sleep(2)
                        move_Photo(lujing)
                        time.sleep(2)
                        break
                quanju_bianliang.accident=1
        else:
            break
        if quanju_bianliang.accident==1:
            quanju_bianliang.accident=0
            break
    driver.switch_to.default_content()