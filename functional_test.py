
import time
import unittest
from selenium import webdriver
from variables import DRIVER_CHROME_FPN

from selenium.webdriver.common.keys import Keys


class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(DRIVER_CHROME_FPN)

    def tearDown(self):
        self.browser.quit()
        self.browser.implicitly_wait(3)

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do", self.browser.title)
        # self.assertIn("local", self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do", header_text)

        input_box = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(input_box.get_attribute("placeholder"), "Enter a to-do item")

        # input_box.send_keys("Buy peacock feathers")
        input_box.send_keys("Use peacock feathers to make a fly")
        input_box.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table(row_text="1: Buy peacock feathers")
        self.check_for_row_in_list_table(row_text="2: Use peacock feathers to make a fly")
        # time.sleep(10)

        self.fail("finish the test")


if __name__ == "__main__":
    unittest.main(warnings="ignore")
