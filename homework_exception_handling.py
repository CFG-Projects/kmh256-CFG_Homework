# Homework: Lesson 8 – Exception Handling
# Question 1
# Simple ATM program
# Using exception handling code blocks such as try/ except / else / finally (NB: the more the better, but try to use at
# least two key words e.g. try/except) write a program that simulates and ATM machine to withdraw money.
# Tasks:
# 1. Prompt user for a pin code
# 2. If the pin code is correct then proceed to the next step, otherwise ask a user to type in a password again.
# You can give a user a maximum of 3 attempts and then exit a program.
# 3. Set account balance to 100.
# 4. Now we need to simulate cash withdrawal
# 5. Accept the withdrawal amount
# 6. Subtract the amount from the account balance and display the remaining balance (NOTE! The balance
# cannot be negative!)
# 7. However, when a user asks to ‘withdraw’ more money than they have on their account, then you need to
# raise an error an exit the program.

account_balance = 100

pin_code = input("Please set your 4-digit PIN: ")
while len(pin_code) < 4 or len(pin_code) > 4 or pin_code.isnumeric() == False:
  print('Invalid PIN')
  pin_code = input("Please set your 4-digit PIN: ")

attempts = 2

user_input = input("Please enter your PIN: ")
while attempts > 0:
  if user_input != pin_code:
    print("Invalid PIN")
    user_input = input("Please enter your PIN: ")
    attempts -= 1
  elif user_input == pin_code:
    break

if user_input != pin_code:
  print("Sorry, you entered the incorrect PIN 3 times")
  quit()

withdrawal_amount = float(input("Please enter the amount you would like to withdraw: "))

if isinstance(withdrawal_amount, float):
  if withdrawal_amount < 0:
    raise ValueError("Sorry, no numbers below zero")
  if account_balance > withdrawal_amount:
    account_balance = account_balance - withdrawal_amount
    print(f'Your remaining balance is £{account_balance}')
  else:
    print(f'You cannot withdraw more money than you have in your account: £{account_balance}')
    raise ValueError("Insufficient funds")
else:
  raise ValueError("Please enter a numerical amount")