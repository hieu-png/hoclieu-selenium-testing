# By nguyen Trung Hieu. Following the guide to create a twitter bot without the need to use twitter official API
import re
import os
import sys
import random

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
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
from util import no_error
from util import passed
# getting config info


SHOULD_LOG = True

# Starting Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

wait_short()

driver.get("https://%s/auth" % (site_url))
# Wait for page to load
wait_short()

try:
    driver.find_element(By.XPATH,
                        "//input[@name='userName']").send_keys(username)
    driver.find_element(By.XPATH,
                        "//input[@type='password']").send_keys(password)
    wait_short()
    driver.find_element(By.XPATH,
                        '//button[@type="submit"]').click()

    wait_short()
    for question in question_list:
        question_name = question[0]
        question_id = question[1]
        try:
            driver.get("https://%s/skill/%s" % (site_url, question_id))
            wait_short()
            show_key_one_button = no_error(driver,
                                           '//button[@title="Hiện đáp án từng ý"]', True)
            show_key_all_button = no_error(driver,
                                           '//button[@title="Hiện đáp án tất cả"]', True)
            fill_in_button = no_error(driver,
                                      '//button[text()="Fill answer"]', False)
            submit_button = no_error(driver,
                                     '//button[text()="Nộp bài"]', False)
            print("%s testing: ShowKeyOne %s | ShowKeyAll %s | Fillin %s | Submit %s" % (
                question_name, passed(show_key_one_button), passed(show_key_all_button), passed(fill_in_button), passed(submit_button)))
            wait_short()
        except Exception as e:
            print(e)

except Exception as e:
    print('error occured')
