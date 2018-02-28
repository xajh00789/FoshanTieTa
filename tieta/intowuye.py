from openwuye import open_wuye
import CommonSeleniumUtil
import time
from selenium.common.exceptions import TimeoutException


def into_wuye(driver):
    try:
        open_wuye(driver)

        all_windows = driver.window_handles
        first_window = driver.current_window_handle
        for window in all_windows:
            if window != first_window:
                second_window = window
                driver.switch_to.window(second_window)

        CommonSeleniumUtil.Clicks(driver,'li[moduleid="200011"] > span')
        time.sleep(3)

        url3='http://pcms.chinatowercom.cn:8880/default/meter/readmeter/MeterReadingList.jsp?_t=313321&_winid=w9696'

        #切换到运营支撑列表系统才能打开抄表记录页面
        driver.switch_to.window(driver.window_handles[2])
        driver.get(url3)
        time.sleep(5)


        third_window_handle=driver.window_handles[2]
        first_window_handle=driver.window_handles[0]
        for handle in driver.window_handles:
            if handle != third_window_handle and handle != first_window_handle:
                driver.switch_to.window(handle)
            #    time.sleep(1)
                driver.close()
        driver.switch_to.window(third_window_handle)


        CommonSeleniumUtil.Clicks(driver, 'a[id="search_btn"] > span')
        time.sleep(2)
        CommonSeleniumUtil.Hoverings(driver, 'span[id="mini-50"] > span > input')
        CommonSeleniumUtil.Clicks(driver, 'span[id="mini-50"] > span > input')
        CommonSeleniumUtil.Hoverings(driver, 'tr[id="mini-52$1"] > td:nth-child(2)')
        CommonSeleniumUtil.Clicks(driver, 'tr[id="mini-52$1"] > td:nth-child(2)')

    except TimeoutException:
        return into_wuye(driver)