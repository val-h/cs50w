import os
import pathlib
import unittest

from selenium import webdriver

driver = webdriver.Chrome()


def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


class WebPageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri('counter.html'))
        self.assertEqual(driver.title, 'Counter')

    def test_increase(self):
        driver.get(file_uri('counter.html'))
        increase = driver.find_element_by_id('increase')
        increase.click()
        self.assertEqual(driver.find_element_by_tag_name('h1').text, "1")

    def test_decrease(self):
        driver.get(file_uri('counter.html'))
        decrease = driver.find_element_by_id('decrease')
        decrease.click()
        self.assertEqual(driver.find_element_by_tag_name('h1').text, "-1")

    def test_multiple_increase(self):
        driver.get(file_uri('counter.html'))
        increase = driver.find_element_by_id('increase')
        for i in range(10):
            increase.click()
        self.assertEqual(driver.find_element_by_tag_name('h1').text, "10")


if __name__ == "__main__":
    unittest.main()
