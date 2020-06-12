import unittest
from selenium import webdriver
from variables import DRIVER_CHROME_FPN


class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.broswer = webdriver.Chrome(DRIVER_CHROME_FPN)

    def tearDown(self):
        self.broswer.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        self.broswer.get("http://localhost:8000")
        # self.assertIn("To-Do", self.broswer.title)
        self.assertIn("local", self.broswer.title)
        self.fail("finishe the test")


if __name__ == "__main__":
    unittest.main(warnings="ignore")