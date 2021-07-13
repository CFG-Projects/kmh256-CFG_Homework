# Homework: Lesson 9 – Unit Testing
# Question 1
# Use Simple ATM program (previous homework) to write unit tests for your functions.
# You are allowed to re-factor your function to ‘untangle’ some logic into smaller blocks of code to 
# make it easier to write tests. 
# Try to write at least 5 unit tests in total covering various cases.

import unittest
from homework_exception_handling import setAccountBalance, setPinCode, withdrawFunds, pinChecker

class TestHomeworkExceptionHandling(unittest.TestCase):

    def test_setAccountBalance(self):
        expected = 100
        result = setAccountBalance(100)
        self.assertEqual(expected, result)
    
    def test_setPinCode(self):
        expected = '9999'
        result = setPinCode() # enter 9999 when prompted to set PIN
        self.assertEqual(expected, result)
    
    def test_pinChecker(self):
        print()
        print('Test 3')
        expected = print("Sorry, you entered the incorrect PIN 3 times")
        result = pinChecker() # enter 0000 3 times when prompted to enter PIN
        self.assertEqual(expected, result)

    def test_withdrawFunds(self):
        print()
        print('Test 4')
        expected = print(f'Your remaining balance is £{50.00 :.2f}')
        result = withdrawFunds(account_balance=100) # enter PIN 9999 then 50 when prompted for amount
        self.assertEqual(expected, result)
    
    # def test_withdrawFunds(self):
    #     print()
    #     print('Test 5')
    #     expected = print(f'Insufficient funds. You cannot withdraw more money than you have in your account: £{100}')
    #     result = withdrawFunds(account_balance=100) # enter PIN 9999 then 110 when prompted for amount
    #     self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()