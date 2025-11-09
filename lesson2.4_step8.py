import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def calc(x:str) -> str:
  return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/explicit_wait2.html')
button = driver.find_element(By.ID, 'book')
WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )

button.click()
x = driver.find_element(By.ID, 'input_value').text
driver.find_element(By.ID, 'answer').send_keys(calc(x))
driver.find_element(By.ID, 'solve').click()
print(driver.switch_to.alert.text)