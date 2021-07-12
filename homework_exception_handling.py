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

def setAccountBalance(amount):
  balance = amount
  return balance

account_balance = setAccountBalance(100)

def setPinCode():
  pin = input("Please set your 4-digit PIN: ")
  while len(pin) < 4 or len(pin) > 4 or not pin.isnumeric():
    print('Invalid PIN')
    pin = input("Please set your 4-digit PIN: ")
  return pin

pin_code = setPinCode()

def withdraw_funds(account_balance):
  withdrawal_amount = input(f'Your balance is £{account_balance}. Please enter the amount you would like to withdraw: ')
  try:
    float(withdrawal_amount)
  except:
    while not withdrawal_amount.isnumeric():
      print("Invalid entry")
      withdrawal_amount = input(f'Your balance is £{account_balance}. Please enter the amount you would like to withdraw: ')
  
  withdrawal_amount = float(withdrawal_amount)

  if isinstance(withdrawal_amount, float):
    if withdrawal_amount < 0:
      raise ValueError("Sorry, no numbers  below zero")
    try:
      if not account_balance >= withdrawal_amount:
        raise Exception
      account_balance = account_balance - withdrawal_amount
      print(f'Your remaining balance is £{account_balance :.2f}')
    except:
      print(f'Insufficient funds. You cannot withdraw more money than you have in your account: £{account_balance}')
  else:
    print("Please enter a numerical amount")

def pinChecker():
  pin_attempts = 2
  print("Your PIN has been set")
  user_input = input("Please enter your PIN: ")
  while pin_attempts > 0:
    try:
      if user_input != pin_code:
        raise Exception
    except:
      print(f'Invalid PIN {pin_attempts} attempt(s) remaining')
      user_input = input("Please enter your PIN: ")
      pin_attempts -= 1
    finally:
      if user_input == pin_code:
        withdraw_funds(account_balance)
        break
  try:
    if user_input != pin_code:
      raise Exception
  except:
    print("Sorry, you entered the incorrect PIN 3 times")
pinChecker()