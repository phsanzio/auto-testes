import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginTest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_sucess(self):
    self.driver.get("http://the-internet.herokuapp.com/login")
    username_input = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    password_input = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )
    username_input.click()
    username_input.send_keys("tomsmith")
    password_input.click()
    password_input.send_keys("SuperSecretPassword!")
    password_input.send_keys(Keys.RETURN)
    message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "flash")))
    self.assertIn("you logged into a secure area!", message.text.lower())

  def test_failure(self):
    self.driver.get("http://the-internet.herokuapp.com/login")
    username_input = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    password_input = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )
    username_input.click()
    username_input.send_keys("PedroSanzio")
    password_input.click()
    password_input.send_keys("LucasMartins")
    password_input.send_keys(Keys.RETURN)
    message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "flash")))
    self.assertIn("your username is invalid!", message.text.lower())

  def tearDown(self):
    self.driver.quit()

if __name__ == "__main__":
  unittest.main()