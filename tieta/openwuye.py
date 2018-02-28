import time
from selenium.common.exceptions import TimeoutException


def open_wuye(driver):
    try:
        url = 'http://app.chinatowercom.cn/bridge/GenerateToken?url=http%3A%2F%2F123.126.34.146%3A20000%2Fuac%2Fweb3%2Fjsp%2Flocal%2Fchnt%2Fchntlogin!ssoLogin.action&'
        newwindow = 'window.open("' + str(url) + '");'
        # print(newwindow)
        driver.execute_script(newwindow)
        time.sleep(3)
    except TimeoutException:
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
