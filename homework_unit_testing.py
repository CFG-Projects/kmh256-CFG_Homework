# Homework: Lesson 9 – Unit Testing
# Question 1
# Use Simple ATM program (previous homework) to write unit tests for your functions.
# You are allowed to re-factor your function to ‘untangle’ some logic into smaller blocks of code to 
# make it easier to write tests. 
# Try to write at least 5 unit tests in total covering various cases.

import unittest
import homework_exception_handling

class TestHomeworkExceptionHandling(unittest.TestCase):

    # enter 9999 when prompted to set / enter PIN
    # enter 50 when prompted for withdrawal amount

    def test_setAccountBalance(self):
        account_balance = homework_exception_handling.setAccountBalance(100)
        self.assertEqual(account_balance, 100)

    def test_setPinCode(self):
        pin_code = homework_exception_handling.setPinCode('9999')
        self.assertEqual(pin_code, '9999')

    def test_pinChecker(self):
        expected = print('Your remaining balance is £50.00')
        self.assertEqual(homework_exception_handling.pinChecker('9999'), expected)

    def test_withdrawFunds(self):
        expected1 = print(f'Your remaining balance is £50.00')
        expected2 = print(f'Insufficient funds. You cannot withdraw more money than you have in your account: £{100}')
        self.assertEqual(homework_exception_handling.withdrawFunds(100), expected1)
        self.assertEqual(homework_exception_handling.withdrawFunds(1), expected2)

if __name__ == '__main__':
    unittest.main()