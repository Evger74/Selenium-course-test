import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):
    def test_of_required_fields(self):
        driver = webdriver.Chrome()
        driver.get('http://suninjuly.github.io/registration1.html')
        first_name = driver.find_element(By.XPATH,
                            "//div[@class='first_block']//input[@class='form-control first']")
        first_name.send_keys('Totoro')
        last_name = driver.find_element(By.XPATH,
                                        "//div[@class='first_block']//input[@class='form-control second']")
        last_name.send_keys('Ghibli')
        email = driver.find_element(By.XPATH, "//input[@class='form-control third']")
        email.send_keys('totoro@ghibli.com')
        driver.find_element(By.CSS_SELECTOR, ".btn").click()
        congrats_text = driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(congrats_text, 'Congratulations! You have successfully registered!',
                         'Registration should be successful')

    def test_missing_field(self):
        driver = webdriver.Chrome()
        driver.get('http://suninjuly.github.io/registration2.html')
        first_name = driver.find_element(By.XPATH,
                                         "//div[@class='first_block']//input[@class='form-control first']")
        first_name.send_keys('Totoro')
        last_name = driver.find_element(By.XPATH,
                                        "//div[@class='first_block']//input[@class='form-control second']")
        last_name.send_keys('Ghibli')
        email = driver.find_element(By.XPATH, "//input[@class='form-control third']")
        email.send_keys('totoro@ghibli.com')
        driver.find_element(By.CSS_SELECTOR, ".btn").click()
        congrats_text = driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(congrats_text, 'Congratulations! You have successfully registered!',
                         'Registration should be successful')


if __name__ == "__main__":
    unittest.main()


