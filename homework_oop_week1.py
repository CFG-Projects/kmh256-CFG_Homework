"""

TASK 1

Write a class to represent a Cash Register.
Your class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self):

        self.total_items = {} # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item):
        print(f'{item}','£{:.2f}'.format(fruits[item]))
        self.total_items[item] = '{:.2f}'.format(fruits[item])
        return self.total_items

    def remove_item(self, item):
        self.total_price = 0
        self.total_items.pop(item)
        return f'The item {item} has been removed from your order'

    def apply_discount(self, percent):
        self.discount = self.total_price * (percent/100)
        self.total_price =- self.discount
        return f'{percent}% discount applied: ''£{:.2f}'.format(self.discount)

    def get_total(self):
        for i in self.total_items.values():
            self.total_price += float(i)
        return 'Total: ''£{:.2f}'.format(self.total_price)

    def show_items(self):
        return f'Your order: {self.total_items}'

    def reset_register(self):
        print('The register has been cleared.')
        self.total_items.clear()
        self.total_price = 0
        self.discount = 0


# EXAMPLE code run:
fruits = {'apples': 2.00, 'bananas': 1.50, 'grapes': 3.20, 'oranges': 2.75,
        'strawberries': 3.45, 'nectarines': 2.45, 'passion fruit': 2.15}

order1 = CashRegister()
order1.add_item('apples')
order1.add_item('bananas')
order1.add_item('grapes')
print(order1.show_items())
print(order1.get_total())
print(order1.remove_item('bananas'))
print(order1.show_items())
print(order1.get_total())
print(order1.apply_discount(10))
print(order1.get_total())
order1.reset_register()
print(order1.show_items())
print(order1.apply_discount(order1.discount))
print(order1.get_total())

print('****************************************************************************')
print('Next Order')
print('****************************************************************************')

order2 = CashRegister()
order2.add_item('nectarines')
order2.add_item('strawberries')
order2.add_item('passion fruit')
print(order2.show_items())
print(order2.get_total())
print(order2.remove_item('nectarines'))
print(order2.show_items())
print(order2.get_total())
print(order2.apply_discount(15))
print(order2.get_total())
order2.reset_register()
print(order2.show_items())
print(order2.apply_discount(order2.discount))
print(order2.get_total())

# ADD
""" Accepts a string item eg. 'apples' from the fruits dictionary.
It then stores the item along with the item price from the fruits dictionary
(key:value pair) inside the total_items dictionary. """

# REMOVE
""" Accepts a string item eg. 'bananas' from the total_items dictionary.
It then removes that key:value pair from the total_items dictionary.
Resets total price to 0 which is then re-calculated when total_items method is called. """

# SHOW ITEMS
""" Returns the total_items dictionary. """

# TOTAL
""" Calculates the sum of the values from the total_items dictionary and returns
the total. """

# DISCOUNT
""" Accepts an integer value as percent discount. Calculates the total - discount
then updates the final total amount. """

# RESET
""" Resets total items to an empty dictionary, total price to zero
and discount to zero."""

print('****************************************************************************')
print()

"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing
a specialization, for example: Software Student and Data Science student. 

"""

class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

class CFGStudent(Student):

    def add_subject(self, subjects_dict):
        print(f'You have added: ')
        for i in subjects_dict:
            self.subjects[i] = subjects_dict[i]
            print(f'{i}: {subjects_dict[i]}%')
        return self.subjects

    def remove_subject(self, subject):
        self.subjects.pop(subject)
        return f'You have removed {subject} from your course list.'

    def view_subjects(self):
        return f'Your courses and grades are: {self.subjects}'

    def get_overall_mark(self):
        overall_marks = 0
        for i in self.subjects.values():
            overall_marks += i
        return f'Overall percentage: {overall_marks / len(self.subjects)}%'

# class CFGStudent(<should inherit from Student>)
student1 = CFGStudent('Kara', 32, 1)
print(f'Name: {student1.name}, Age: {student1.age}, ID: {student1.id}')

# create new methods that manage student's subjects
# add new subject and its grade to the dict
s1_subjects_dict = {'Python': 86, 'SQL': 73, 'Software Development': 67,
'JavaScript': 69, 'OOP': 74}
student1.add_subject(s1_subjects_dict)

# create a method to view all subjects taken by a student
print(student1.view_subjects())
student1.add_subject({'Project': 78})
print(student1.view_subjects())

# remove subject and its grade to the dict
print(student1.remove_subject('JavaScript'))
print(student1.view_subjects())

# create a method (and a new variable) to get student's overall mark (use average)
print(student1.get_overall_mark())

# ADD
""" Accepts a dictionary of subjects and grades.
It then iterates through the dictionary and adds each item to the subjects dictionary. """

# REMOVE
""" Accepts a string item eg. 'JavaScript' from the subjects_dict.
It then removes that key:value pair from the subjects dictionary. """

# VIEW SUBJECTS
""" Returns the subjects dictionary. """

# OVERALL MARK
""" Calculates the overall mark by iterating through the subjects dictionary values
and storing the sum in the overall_mark variable. It then calculates the average grade
by dividing overall_mark by the length of the values list and returns the result."""