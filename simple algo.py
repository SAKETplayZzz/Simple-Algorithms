import colorama
from colorama import Fore
colorama.init(autoreset=True)

def POSorNEG():
   num_NoP = float(input("Enter a number: "))
   if num_NoP > 0:
      print("Your number is a positive number")
   elif num_NoP == 0:
      print("Your number is Zero, zero is not positive or negative")
   else:
      print("Your number is a negative number")

def RAD():
   numr = float(input("Your Radius: "))
   cal = (3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679*numr*numr)
   print('Area of the circle is: ' and cal)

def Grt_Les():
   numGrt_Les1 = int(input('Enter first number: '))
   numGrt_Les2 = int(input("Enter second number: "))
   print(' ')
   if numGrt_Les1 >= numGrt_Les2:
      if numGrt_Les1 == numGrt_Les2:
         print("Both numbers are equal.")
      else:
         print("Fisrt number is greater than the second number.")
   else:
      print("Second number is greater than the First number.")


def CALCU():
   def add(num1, num2):
      return num1 + num2

   def subtract(num1, num2):
      return num1 - num2

   def multiply(num1, num2):
      return num1 * num2

   def divide(num1, num2):
      return num1 / num2

   print("Please select operation -\n" 
         "1. Add\n" 
         "2. Subtract\n" 
         "3. Multiply\n" 
         "4. Divide\n")

   select = int(input("Select operations form 1, 2, 3, 4 :"))

   number_1 = int(input("Enter first number: "))
   number_2 = int(input("Enter second number: "))

   if select == 1:
      print(number_1, "+", number_2, "=",
            add(number_1, number_2))

   elif select == 2:
      print(number_1, "-", number_2, "=",
            subtract(number_1, number_2))

   elif select == 3:
      print(number_1, "*", number_2, "=",
            multiply(number_1, number_2))

   elif select == 4:
      print(number_1, "/", number_2, "=",
            divide(number_1, number_2))
   else:
      print("Invalid input")

print(' ')
print(Fore.LIGHTCYAN_EX+ '~~~Type any one of the following options numbers to proceed~~~')
print(Fore.LIGHTGREEN_EX +'(option 1)','- Algorithm for finding if a number is a Positive or a Negative')
print(Fore.LIGHTGREEN_EX +'(option 2)','- Algorithm for finding the Radius of a circle')
print(Fore.LIGHTGREEN_EX +'(option 3)','- Algorithm for finding the Greater number')
print(Fore.LIGHTGREEN_EX +'(option 4)','- Algorithm for a simple Calculator')
print(' ')

introQ = input('Type option number: ')
if introQ == '1':
   POSorNEG()
if introQ == '2':
   RAD()
if introQ == '3':
   Grt_Les()
if introQ == '4':
   CALCU()
if introQ == '/github':
   print('https://github.com/SAKETplayZzz/Simple-Algorithms')

Dragger = input()
