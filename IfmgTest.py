import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IfmgTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.ifmg.edu.br/sabara")

    def test_menu_links(self):
        menu_links = [
            "portalservicos-pdi",
            "portalservicos-cpa-1",
            "portalservicos-meu-ifmg",
            "portalservicos-ex-alunos",
            "portalservicos-acesso-a-sistemas",
            "portalservicos-area-de-imprensa",
            "portalservicos-ouvidoria",
            "portalservicos-fale-conosco",
            "portalservicos-webmail",
            "portalservicos-sala-virtual-ead"
        ]

        for links in menu_links:
            with self.subTest(link=links):
                link = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, links))
                )
                self.assertTrue(link.is_displayed())

    def test_search(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "nolivesearchGadget"))
        )
        search_button.click()
        search_button.clear()
        search_button.send_keys("edital")
        search_button.send_keys(Keys.RETURN)

        search = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "search-term"))
        )
        self.assertTrue(search.is_displayed())
        self.assertIn("edital", search.text.lower())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
