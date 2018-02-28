import CommonSeleniumUtil
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import quanju_bianliang

#翻页
def fanye(driver,page):
    try:
        print("翻页")
        time.sleep(2)
        CommonSeleniumUtil.keyboardAction(driver,'input[class="mini-pager-num"]','a')
        CommonSeleniumUtil.keyboardAction_BACKSPACE(driver,'input[class="mini-pager-num"]')
        CommonSeleniumUtil.TypeIns(driver,'input[class="mini-pager-num"]',str(page))
        CommonSeleniumUtil.keyboardAction_ENTER(driver,'input[class="mini-pager-num"]')

    except TimeoutException:
        return fanye()


def fanye2(driver,page):
    try:

        print("翻页")
        CommonSeleniumUtil.keyboardAction(driver, 'input[class="mini-pager-num"]', 'a')
        CommonSeleniumUtil.keyboardAction_BACKSPACE(driver, 'input[class="mini-pager-num"]')
        CommonSeleniumUtil.TypeIns(driver, 'input[class="mini-pager-num"]', str(page))
        CommonSeleniumUtil.keyboardAction(driver, 'input[class="mini-pager-num"]', 'a')
        CommonSeleniumUtil.keyboardAction(driver, 'input[class="mini-pager-num"]', 'x')
        CommonSeleniumUtil.keyboardAction(driver, 'input[class="mini-pager-num"]', 'v')
        CommonSeleniumUtil.keyboardAction_ENTER(driver, 'input[class="mini-pager-num"]')

        time.sleep(3)
        WebDriverWait(driver, 20, 0.5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[contains(text(),"4406")]')))
        element = driver.find_elements_by_xpath('//div[contains(text(),"4406")]')
        print(len(element))
        time.sleep(4)
        zhandian_bianma = []
        for i in element:
            # print(i.text)
            zhandian = i.text
            zhandian_bianma.append(zhandian)
        return zhandian_bianma
    except TimeoutException:
        return fanye2()
