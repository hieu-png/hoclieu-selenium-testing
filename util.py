import time
from config import SHORT_WAITING_TIME
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


def evaluation(driver, xPath, reClick):
    try:
        button = None
        try:
            button = driver.find_element(By.XPATH, xPath)
        except NoSuchElementException:
            return 'not exist'

        driver.execute_script("document.getElementById('skill-wrapper').scrollTo(0, 3000)")

        button.click()
        wait_short()
        driver.find_element(By.XPATH,
                            '//div[text()="Lỗi dữ liệu câu hỏi"]')
        wait_short()
    except NoSuchElementException:
        if reClick:
            button.click()
        return 'passed'
    return 'not passed'


def wait_short():
    time.sleep(SHORT_WAITING_TIME)
