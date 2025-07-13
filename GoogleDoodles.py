import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleDoodles(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_ex01(self):
    self.driver.get("https://www.google.com")
  
    estou_com_sorte_button = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='Estou com sorte']"))
    )
    self.driver.execute_script("arguments[0].click();", estou_com_sorte_button)
    WebDriverWait(self.driver, 10).until(EC.title_contains("Google Doodles"))
    self.assertIn("Google Doodles", self.driver.title)
  
  def tearDown(self):
    self.driver.quit()

if __name__ in "__main__":
  unittest.main()