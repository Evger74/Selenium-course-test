import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x:str) -> str:
  return str(math.log(abs(12*math.sin(int(x)))))


chrome = webdriver.Chrome()
try:
    chrome.get('http://suninjuly.github.io/alert_accept.html')
    chrome.find_element(By.CSS_SELECTOR, '.btn').click()
    confirm = chrome.switch_to.alert
    confirm.accept()
    x = chrome.find_element(By.ID, 'input_value').text
    chrome.find_element(By.ID, 'answer').send_keys(calc(x))
    chrome.find_element(By.CSS_SELECTOR, '.btn').click()

finally:
    time.sleep(10)
    chrome.quit()





