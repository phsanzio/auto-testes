import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleDoodles(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()

  def ex01(self):
    self.driver.get("https://www.google.com")
    estou_com_sorte_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Estou com sorte']"))
    )
    estou_com_sorte_button.click()
    WebDriverWait(self.driver, 10).until(EC.title_contains("Google Doodles"))
    self.assertIn("Google Doodles", self.driver.title)


if __name__ in "__main__":
  unittest.main()