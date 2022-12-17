# By nguyen Trung Hieu. Following the guide to create a twitter bot without the need to use twitter official API
import re
import os
import sys
import random

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import selenium

# Config.py

from config import question_list
from config import site_url
# credential.py

from credential import username
from credential import password

# SpecificConfig.py

# Util.py
from util import wait_short
from util import evaluation
# getting config info
# hide log from driver
os.environ['WDM_LOG'] = '0'
SHOULD_LOG = True
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--kiosk")

# Starting Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options)
wait_short()
QUESTION_LIST_LENGTH = len(question_list)
driver.get("https://%s/auth" % (site_url))
# Wait for page to load
wait_short()
print('Started skill testing. Number of test to be done: %s' %
      (QUESTION_LIST_LENGTH))
try:
    driver.find_element(By.XPATH,
                        "//input[@name='userName']").send_keys(username)
    driver.find_element(By.XPATH,
                        "//input[@type='password']").send_keys(password)
    wait_short()
    driver.find_element(By.XPATH,
                        '//button[@type="submit"]').click()

    wait_short()
    test_ok_count = 0
    for question in question_list:
        question_name = question[0]
        question_id = question[1]
        try:
            driver.get("https://%s/skill/%s" % (site_url, question_id))
            wait_short()
            show_key_one_button = evaluation(driver,
                                             '//button[@title="Hiện đáp án từng ý"]', True)
            show_key_all_button = evaluation(driver,
                                             '//button[@title="Hiện đáp án tất cả"]', True)
            fill_in_button = evaluation(driver,
                                        '//button[text()="Fill answer"]', False)
            submit_button = evaluation(driver,
                                       '//button[text()="Nộp bài"]', False)
            is_ok = show_key_all_button != 'not passed' and show_key_one_button != 'not passed' and fill_in_button != 'not passed' and submit_button != 'not passed'
            if is_ok:
                test_ok_count += 1
            print("%s: %s testing: ShowKeyOne %s | ShowKeyAll %s | Fillin %s | Submit %s" % (
                'OK' if is_ok else 'NOK', question_name, show_key_one_button, show_key_all_button, fill_in_button, submit_button))
            wait_short()
        except Exception as e:
            print(e)
    print("%d test done! %s test(s) passed and %s test(s) not passed" %
          (QUESTION_LIST_LENGTH, test_ok_count, QUESTION_LIST_LENGTH-test_ok_count))
except Exception as e:
    print('error occured')
