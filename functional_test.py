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

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do", self.browser.title)
        # self.assertIn("local", self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do", header_text)

        input_box = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(input_box.get_attribute("place_holder"), "Enter a to-do item")

        input_box.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(any(row.text == "1: Buy a peacock feathers" for row in rows))

        self.fail("finish the test")


if __name__ == "__main__":
    unittest.main(warnings="ignore")
