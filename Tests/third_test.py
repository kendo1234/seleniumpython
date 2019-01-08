import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


# This is the first test, but with benchmarking
class timed_search(unittest.TestCase):

    def setUp(self):
        self.startTime = time.time()

    def test_url_timed(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.driver.set_window_size(1120, 550)
        self.driver.get("http://duckduckgo.com/")
        self.driver.find_element_by_id(
            'search_form_input_homepage').send_keys("realpython")
        self.driver.find_element_by_id("search_button_homepage").click()
        self.assertIn(
            "https://duckduckgo.com/?q=realpython", self.driver.current_url
        )

    def tearDown(self):
        t = time.time() - self.startTime
        print("%s: %.3f" % (self.id(), t))
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
