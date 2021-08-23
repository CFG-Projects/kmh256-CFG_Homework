"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""
import random

class CFGStudent:

    def __init__(self, name, surname, age, email):
        # attributes name, surname, age, email, student id
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = str(random.randint(1000, 10000))

    @staticmethod
    def generate_id(self, student_id):
        #'create a random new id, which is any number between 1,000 and 10,000'
        #'return id as a string'
        self.student_id = str(random.randint(1000, 10000))
        return student_id

    def get_id(self):
        # method to fetch student’s id
        return self.student_id

    def get_fullname(self):
        # methods to fetch student’s full name
        return f'{self.name} {self.surname}'


class NanoStudent(CFGStudent):

    def __init__(self, specialization, name, surname, age, email):
        # same attributes as its parent class
        # additional attributes ‘specialization’ and course grades
        self.specialization = specialization
        self.course_grades = dict()
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = 0

    @staticmethod
    def generate_id(self, student_id):
        #create a random new id, which is a word NANO followed by any number between 1,000 and 10,000'
        #return id as a string'
        self.student_id = f'NANO {random.randint(1000, 10000)}'
        return student_id

    def add_new_grade(self, course_grades):
        #pass in a task name and its grade, so that both are added to course_grades
        print(f'You have added: ')
        #for i in course_grades:
            #self.course_grades[i] = course_grades[i]
            #print(f'{i}: {course_grades[i]}%')
        self.course_grades = course_grades
        return self.course_grades

    def get_course_grades(self):
        return f'Your courses and grades are: {self.course_grades}'


############################################

# Example run

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}


"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""

def even_fibonacci_sum(limit):
  a, b = 1, 1
  total = 0
  count = 0

  while count < limit:
    if a % 2 == 0:
      total += a
    a, b = b, a+b
    count +=1
  return total

##### TESTS ####

print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))   # should be 0

"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution.

"""

def is_valid_subsequence(arr, seq):

  arr_index = 0
  seq_index = 0

  while arr_index < len(arr) and seq_index <len(seq):

    if arr[arr_index] == seq[seq_index]:
      seq_index +=1
      arr_index +=1

    return seq_index == len(seq)

#### TESTS ####

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE



"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)


The Employee class violates the Single Responsibility Principle - 
this states that classes should have one responsibility.
Here there are two responsibilities: updating department information in the database and 
employee properties management.

It is a rigid system as if the application changes and database management functions are impacted,
the classes that use employee properties will have to be changed.
For this to meet SRP, another class that handles the responsibility of storing an employee to the database
should be created.

"""

