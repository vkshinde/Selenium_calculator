from selenium import webdriver
import time
import unittest


class UITesting:
    def __init__(self, driver, numbers, operators):
        # The number is a parameter and contains elements. These elements represent the calculator's digits. it is a list.
        # The operator is also a list and contains operator elements such as (/, *, +, -).
        # The order of the elements that are stored in the list is not correct so I have used the following method to organize the elements.
        numbers.reverse()
        numbers[2:5] = numbers[2:5][::-1]
        numbers[5:8] = numbers[5:8][::-1]
        numbers[8:11] = numbers[8:11][::-1]
        numbers.append(numbers.pop(0))
        # initilization 
        self.numbers = numbers
        self.driver = driver
        self.operators = operators
       

    def normal_number(self, x):
        if x != '.':
            self.numbers[int(x)].click()
        else:
            self.numbers[10].click()

    def negative_num(self, num):
        
        # If any of the operands is a negative number, this method will be invoked to enter the correct data.
        # This method will take the number as a parameter and put a negative sign in front of the number.
        self.operators[2].click()
        [self.numbers[int(x)].click() if x != '-' else self.operators[2].click() for x in
         str(num)[1:]]




    def add(self, first_num, second_num):
        # Addition Method 
        # list Comprehension

        set_resolve = [[self.normal_number(x) for x in str(first_num)] if first_num > 0 else
                       self.negative_num(first_num)]
        self.operators[0].click()

        second_set_resolve = [
            [self.normal_number(x) for x in str(second_num)] if second_num > 0 else
            self.negative_num(second_num)]
        input_data = self.driver.find_element_by_id('sciInPut').text
        # Check whether the input data and the entered data are correct.
        if input_data == f' {first_num} + {second_num}':
            print("UI is Working")
        time.sleep(1)
        # return the output
        return self.driver.find_element_by_id('sciOutPut').text

    def multiplication(self, first_num, second_num):
        # Multiplication method
        set_resolve = [[self.normal_number(x) for x in str(first_num)] if first_num > 0 else
                       self.negative_num(first_num)]

        self.operators[4].click()

        second_set_resolve = [
            [self.normal_number(x) for x in str(second_num)] if second_num > 0 else
            self.negative_num(second_num)]
        input_data = self.driver.find_element_by_id('sciInPut').text
        if input_data == f' {first_num} × {second_num}':
            print("UI is Working")
        time.sleep(1)
        return self.driver.find_element_by_id('sciOutPut').text

    def division(self, first_num, second_num):
        # Division method
        set_resolve = [[self.normal_number(x) for x in str(first_num)] if first_num > 0 else
                       self.negative_num(first_num)]

        self.operators[7].click()

        second_set_resolve = [
            [self.normal_number(x)for x in str(second_num)] if second_num > 0 else
            self.negative_num(second_num)]
        input_data = self.driver.find_element_by_id('sciInPut').text
        if input_data == f' {first_num} ÷ {second_num}':
            print("UI is Working")
        time.sleep(1)
        return self.driver.find_element_by_id('sciOutPut').text

    def sub(self, first_num, second_num):
        # Substraction method
        set_resolve = [[self.normal_number(x) for x in str(first_num)] if first_num > 0 else
                       self.negative_num(first_num)]

        self.operators[2].click()

        second_set_resolve = [
            [self.normal_number(x) for x in str(second_num)] if second_num > 0 else
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

