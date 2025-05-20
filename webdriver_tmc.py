from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

def run_tmc_task():
    driver = webdriver.Edge()  # ou configure avec Service(...) si nécessaire

    driver.get("https://us.cloud.talend.com")
    time.sleep(5)

    email_input = driver.find_element(By.ID, "1-email")
    email_input.send_keys("houssemdammak800@gmail.com")

    password_input = driver.find_element(By.ID, "1-password")
    password_input.send_keys("HD@olive2025")
    password_input.send_keys(Keys.RETURN)
    time.sleep(10)

    driver.get("https://app.us.cloud.talend.com/tmc/tasks-and-plans-administration/6826ed1da15ba857fedf20e6/6826ed1da15ba857fedf20e7/tasks/standard/6826f0ba5e2ff374402cd151/detail")
    time.sleep(5)

    execute_button = driver.find_element(By.ID, "task-details-run-now")
    execute_button.click()

    time.sleep(5)
    driver.quit()
