# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
        """Identifying my name"""
        user_name = 'travis'.title()
        print("Hello " + user_name + "!")

hello_name('user_name')
              
# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
        for number in range(1,101,2):
               print (number)
first_odds()
# This should satisfy question 2, but the word return makes me think you want to have nothing print so that code is next:

def first_odds():
        for number in range(1,101,2):
               return(number) * 0
        print (number)
first_odds()   
               
# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(list):
        max = list[0]
        for a in list:
            if a > max:
                   max = a
                   return max
print(max_num_in_list([5,77,-3,8]))


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

    
def is_leap(year):
  leap = False

  if (year % 4 == 0) and (year % 100 != 0): 
      leap = True
  elif (year % 100 == 0) and (year % 400 != 0):
      leap = False
  elif (year % 400 == 0):
      leap = True
  else:
      leap = False

  return leap
year=2023
print (is_leap(year))


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def are_consecutive_numbers(list):
    list.sort()
    num = list[0]

    for i in range(1, len(list)):
        if list[i] != num + i:
            return False
    
    return True
num = [2, 3, 4, 5, 6, 8]
print (are_consecutive_numbers(num))

#I had to get alot of help with this one on the internet. For my understanding: list[i] is cycling through each number with num + 1 and if found accurate continues as True, and when it reaches 8 the value is false.
#A return is the value of the equation being done. ex. num + i the first result would be 2+1=3 therefore the return is 3. Am i correct in saying this?