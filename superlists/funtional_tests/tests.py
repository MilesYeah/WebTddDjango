import time

import unittest
from selenium import webdriver
from funtional_tests.variables import DRIVER_CHROME_FPN
from django.test import LiveServerTestCase

from selenium.webdriver.common.keys import Keys


class NewVistorTest(LiveServerTestCase):

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
        s1 = "Buy peacock feathers"
        s2 = "use peacock feathers to make a fly"
        s3 = "buy milk"

        self.browser.get(self.live_server_url)
        self.assertIn("To-Do", self.browser.title)
        # self.assertIn("local", self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do", header_text)

        input_box = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(
            input_box.get_attribute("placeholder"),
            "Enter a to-do item"
        )

        input_box.send_keys(s1)
        input_box.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, "/lists/.+")
        time.sleep(1)
        self.check_for_row_in_list_table(row_text=f"1: {s1}")

        input_box = self.browser.find_element_by_id("id_new_item")
        input_box.send_keys(s2)
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table(row_text=f"2: {s2}")
        self.check_for_row_in_list_table(row_text=f"1: {s1}")
        # time.sleep(10)

        self.browser.quit()
        self.browser = webdriver.Chrome(DRIVER_CHROME_FPN)

        self.browser.get(self.browser.current_url)
        page_text = self.browser.find_element_by_tag_name("body").text
        self.assertIn(s1, page_text)
        self.assertIn(s2, page_text)

        input_box = self.browser.find_element_by_id("id_new_item")
        input_box.send_keys(s3)
        input_box.send_keys(Keys.ENTER)

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, "/lists/.+")
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn(s1, page_text)
        self.assertIn(s3, page_text)

        self.fail("finish the test")


if __name__ == "__main__":
    unittest.main(warnings="ignore")
