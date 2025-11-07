import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


chrome = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
try:
    chrome.get(link)
    num1 = chrome.find_element(By.ID, "num1").text
    num2 = chrome.find_element(By.ID, "num2").text
    result = str(int(num1) + int(num2))
    select_el = Select(chrome.find_element(By.TAG_NAME, "select"))
    select_el.select_by_value(result)
    chrome.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    chrome.quit()
