"""print(self.add(6, 3))
driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()
print(self.sub(6, 3))
driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()
print(self.multiplication(6, 3))
driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()
print(self.division(6, 3))
driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()"""
import Main_Module
chrome_elements = Main_Module.open_chrome()
ui_testing = Main_Module.UITesting(chrome_elements[0], chrome_elements[1], chrome_elements[2])
print()