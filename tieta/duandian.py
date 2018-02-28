from fanyeExample import fanye,fanye2
from intowuye import into_wuye
from checkdetailinform import check_detail_inform
import time
import quanju_bianliang

def duandian_spider(driver,page_start,page_end):
    #  check_detail_inform()
    i=page_start
    while(i<page_end):
        try:
            print("正在下载第%d页图片"%i)
            if quanju_bianliang.fault_happen==True:
                fanye(driver,i-1)
                time.sleep(2)
                zhandian_bianma=fanye2(driver,i)
            else:
                zhandian_bianma=fanye2(driver,i)  # 翻开新的一页
            time.sleep(4)
            check_detail_inform(zhandian_bianma,driver)  # 继续查看详细页面
            i+=1
            quanju_bianliang.fault_happen=False
        except Exception as e:
            print(e)
            str2='Message: unexpected alert open'
            if str2 in str(e):
                driver.switch_to.alert.accept()
            print("爬取第%d页出现错误"%i)
            quanju_bianliang.fault_happen=True
            first_handle=driver.window_handles[0]
            for handle in driver.window_handles:
                if handle != first_handle:
                     driver.switch_to.window(handle)
                     time.sleep(2)
                     driver.close()
            driver.switch_to.window(driver.window_handles[0])

            into_wuye(driver)
