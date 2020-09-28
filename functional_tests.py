from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title_is_kevin_rz(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Kevin RZ', self.browser.title)

    def test_homepage_contain_name_kevin_raikhan_zain(self):
        self.browser.get('http://localhost:8000')
        name = self.browser.find_element_by_id("full_name").text
        self.assertIn('Kevin Raikhan Zain', name)


if __name__ == '__main__':
    unittest.main()
