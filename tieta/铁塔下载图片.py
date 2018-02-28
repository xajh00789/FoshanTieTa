from selenium import webdriver
import CommonSeleniumUtil
from intowuye import into_wuye
from duandian import duandian_spider

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': r'E:\迅雷下载\铁塔图片\临时图片3'

         }
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=options)

#http://pcms.chinatowercom.cn:8880/default/meter/readmeter/MeterReadingList.jsp?_t=313321&_winid=w9696



#进入主页
def search():
    driver.get('http://eip.chinatowercom.cn')
    CommonSeleniumUtil.TypeIns(driver, '#username', '')
    CommonSeleniumUtil.TypeIns(driver,'#password','')
    CommonSeleniumUtil.Clicks(driver, 'button[value="登 录"]')
    into_wuye(driver)

def main():
    search()
   # print(driver.page_source.encode('utf-8').decode(), file=open("2.html", "w", encoding='utf-8'))
    totalpage=CommonSeleniumUtil.InformationAcquisition(driver,'span[class="mini-pager-pages"]')
    page=int(totalpage[2:].strip())
    page_start=1
    if page%2==0:
        page_end=page//2
    else:
        page_end=page//2+1
    print("爬取一共%d页"%page_start)
    duandian_spider(driver,page_start,page_end)


main()


