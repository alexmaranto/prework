# Question 1: Write a function to print "hello_USERNAME!"
# USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
     print("hello_" + user_name + "!")

hello_name("Alex".upper())



# Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
     odd_numbers = list(range(1,101,2))
     print(odd_numbers)

first_odds()

    

# Question 3: Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    for num in a_list:
      if len(a_list) == 0:
         return None
      else:
          return max(a_list)
      
a_list= [5, 3, 6, 2, 10, 14, 4]

max_num_in_list(a_list)
print(max_num_in_list(a_list))


# Question 4: Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
     if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0):
          return True
     else:
          return False
     
a_year = 2024
is_leap_year(a_year)    
print(is_leap_year(a_year))



# Question 5: Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type.

def is_consecutive(a_list):
    if len(a_list) <= 1:
        return True

    sorted_numbers = sorted(a_list)
    start_number = sorted_numbers[0]

    for x in range(1, len(sorted_numbers)):
        if sorted_numbers[x] != start_number + x:
            return False

    return True
a_list = [1, 2, 3, 4, 5]
print(is_consecutive(a_list))