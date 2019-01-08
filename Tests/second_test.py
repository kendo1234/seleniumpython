import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class button_association_check(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.driver.set_window_size(1120, 550)

    def test_url(self):
        self.driver.get("https://app.simplegoods.co/i/IQCZADOY") # url associated with button click
        button = self.driver.find_element_by_id("payment-submit").get_attribute("value")
        self.assertEquals(u'Pay - $60.00', button)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()