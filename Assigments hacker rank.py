'''
1.Take values of length and breadth of a rectangle from user and check if it is a square or not.
'''

def square(len,bre):
    if len == bre :
        print("Yes")
    else :
      print("No") 

Length = int(input())
breath = int(input())
square(Length,breath)

#--------------------------------------------------------------------------------------------------
'''
2.Our college decided to give bonus of 5% to employees of VBIT if his/her year of service is more than 5 years. Ask employee for their salary and year of service 
  and print the net bonus amount. **
'''

def bonuss(salary,year):
    bonus = salary*5/100
    if years >= 5:
      print("Bonus is", round(bonus))
    else :
       print("No Bonus")
sal = int(input())
years = int(input())
bonuss(sal,years)

#-----------------------------------------------------------------------------------------------
'''
3.Print the first ten multiples of any integer N using while loop.
'''
def cali(num_1) :
   i = 1
   while i<= 10:
       result = num_1*i
       i = i + 1
       print(result)


num_2 = int(input())
cali(num_2)

#-------------------------------------------------------------------------------------------------
'''
4.Write a program that accepts words to form a string using the for loop.Print the reversed result.
'''
def reverse(strings):
    str = ""
    for i in strings:
      str = i + strings
    print(str)


string = input()
reverse(string)

#----------------------------------------------------------------------------------------------------
'''
5.Arguments: name and age. Using Functions,print the values in the following order.
'''
def strings(name,age):
  print(name + " " + age)

names = input()
ag = input()
strings(names,ag)
