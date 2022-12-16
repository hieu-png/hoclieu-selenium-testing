import time
from config import SHORT_WAITING_TIME
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def no_error(driver, xPath, reClick):
    try:
        try:
            button = driver.find_element(By.XPATH, xPath)
        except:
            print('error encountered')
        button.click()
        wait_short()
        driver.find_element(By.XPATH,
                            '//div[text()="Lỗi dữ liệu câu hỏi"]')
        wait_short()
    except NoSuchElementException:
        if reClick:
            button.click()
        return True
    return False


def wait_short():
    time.sleep(SHORT_WAITING_TIME)


def passed(bool):
    if bool:
        return 'passed'
    else:
        return 'not passed'
