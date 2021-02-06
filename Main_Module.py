from selenium import webdriver
import time
import unittest


class UITesting:
    def __init__(self, driver, numbers, operators):
        numbers.reverse()
        numbers[2:5] = numbers[2:5][::-1]
        numbers[5:8] = numbers[5:8][::-1]
        numbers[8:11] = numbers[8:11][::-1]
        numbers.append(numbers.pop(0))

        self.numbers = numbers
        self.driver = driver
        self.operators = operators


    def negative_num(self, num):
        self.operators[2].click()
        [self.numbers[int(x)].click() if x != '-' else self.operators[2].click() for x in
         str(num)[1:]]

    def add(self, first_num, second_num):

        set_resolve = [[self.numbers[int(x)].click() for x in str(first_num)] if first_num > 0 else
                       self.negative_num(first_num)]
        self.operators[0].click()

        second_set_resolve = [
            [self.numbers[int(x)].click() for x in str(second_num)] if second_num > 0 else
            self.negative_num(second_num)]
        input_data = self.driver.find_element_by_id('sciInPut').text
        if input_data == f' {first_num} + {second_num}':
            print("UI is Working")
        time.sleep(1)

        return self.driver.find_element_by_id('sciOutPut').text

    def multiplication(self, first_num, second_num):

        set_resolve = [[self.numbers[int(x)].click() for x in str(first_num)] if first_num > 0 else
                       self.negative_num(first_num)]

        self.operators[4].click()

        second_set_resolve = [
            [self.numbers[int(x)].click() for x in str(second_num)] if second_num > 0 else
            self.negative_num(second_num)]
        input_data = self.driver.find_element_by_id('sciInPut').text
        if input_data == f' {first_num} × {second_num}':
            print("UI is Working")
        time.sleep(1)
        return self.driver.find_element_by_id('sciOutPut').text

    def division(self, first_num, second_num):

        set_resolve = [[self.numbers[int(x)].click() for x in str(first_num)] if first_num > 0 else
                       self.negative_num(first_num)]

        self.operators[7].click()

        second_set_resolve = [
            [self.numbers[int(x)].click() for x in str(second_num)] if second_num > 0 else
            self.negative_num(second_num)]
        input_data = self.driver.find_element_by_id('sciInPut').text
        if input_data == f' {first_num} ÷ {second_num}':
            print("UI is Working")
        time.sleep(1)
        return self.driver.find_element_by_id('sciOutPut').text

    def sub(self, first_num, second_num):

        set_resolve = [[self.numbers[int(x)].click() for x in str(first_num)] if first_num > 0 else
                       self.negative_num(first_num)]

        self.operators[2].click()

        second_set_resolve = [
            [self.numbers[int(x)].click() for x in str(second_num)] if second_num > 0 else
            self.negative_num(second_num)]
        input_data = self.driver.find_element_by_id('sciInPut').text
        if input_data == f' {first_num} − {second_num}':
            print("UI is Working")
        time.sleep(1)
        return self.driver.find_element_by_id('sciOutPut').text


def open_chrome(website='https://calculator.net'):
    # Open Chrome Browser (If the code does not work please change the path to the path where you have stored your
    # web driver
    driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
    driver.get(website)
    numbers = driver.find_elements_by_class_name('scinm')
    operators = driver.find_elements_by_class_name('sciop')
    input_data = driver.find_element_by_id('sciInPut')

    return [driver, numbers, operators]

    time.sleep(2)


"""""
423 525 Multiplication 222075
4000 200 Division 20
-234234 345345 Addition 111111
234823 -23094823 Subtraction 23329646
"""""

