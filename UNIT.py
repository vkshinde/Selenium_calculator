import Main_Module
import unittest

chrome_elements = Main_Module.open_chrome()
ui_testing = Main_Module.UITesting(chrome_elements[0], chrome_elements[1], chrome_elements[2])


class Testing(unittest.TestCase):
    def test_add(self):
        self.assertEqual(int(ui_testing.add(-234234, 345345)), 111111)
        chrome_elements[0].find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()

    def test_sub(self):
        self.assertEqual(int(ui_testing.sub(234823, -23094823)), 23329646)
        chrome_elements[0].find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()

    def test_multiplication(self):
        self.assertEqual(int(ui_testing.multiplication(423, 525)), 222075)
        chrome_elements[0].find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()

    def test_division(self):
        self.assertEqual(int(ui_testing.division(4000, 200)), 20)
        chrome_elements[0].find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()


if __name__ == '__main__':
    unittest.main()
