import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
try:
    chrome.get("http://suninjuly.github.io/file_input.html")
    chrome.find_element(By.NAME, "firstname" ).send_keys("Totoro")
    chrome.find_element(By.NAME, "lastname").send_keys("Ghibli")
    chrome.find_element(By.NAME, "email").send_keys("Totoro@email...ccoomm")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "some_text.txt")
    chrome.find_element(By.ID, "file").send_keys(file_path)
    chrome.find_element(By.CSS_SELECTOR, ".btn").click()


finally:
    time.sleep(10)
    chrome.quit()