import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


chrome = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

try:
    chrome.get(link)
    x_element = chrome.find_element(By.ID, "input_value").text
    x = calc(x_element)
    button = chrome.find_element(By.TAG_NAME, "button")
    chrome.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    chrome.find_element(By.ID, "answer").send_keys(x)
    chrome.find_element(By.ID, "robotCheckbox").click()
    chrome.find_element(By.ID, "robotsRule").click()
    chrome.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(10)
    chrome.quit()