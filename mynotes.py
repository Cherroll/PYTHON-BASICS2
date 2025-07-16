'''
age = 20
age =19.95
first_name ="Mpho"
is_online =True
print(age)

name = input("What is your name? ") #returns a string 
print("Hello " + name) 

birth_year =input("What is your birth year? ")

age =2020-int(birth_year) #converting a string into an integer using int
print(age)

float()  #a number with a decimal point 
bool() #converting a value to a boolean 
str()
sum = 10.1 + 20
print(sum)

first= input("First")
second= input("Second")
sum= float(first) + float(second)
print("Sum: "+str(sum))
 
course = 'Python for beginners'
print(course.replace('for','4'))
print(course.find('o'))

study = "Mpho is a hard worker"
print("Mpho" in study) #boolean

temperature =25
if temperature >30:
    print("It's a hot day")
elif temperature >20:
    print("It's  a nice day")
elif temperature >10:
    print("It's a bit cold")
else:  #for else statement you don't write a condition
    print("It's really  cold")
    
weight =int(input("Weight: "))
unit =input("(K)g or (L)bs: ")
if unit.upper() == "K":
        converted = weight /0.45
        print("Weight in Lbs: " + str(converted))
else:
        converted = weight* 0.45
        print("Weight in Kgs: " + str(converted))
        
i =1
while i <= 10:
    print(i*'*')
    i =i +1
#lists
names =["John","Mpho","Scooby"]
print(names[0:1]) #returns john and Mpho
#loops
numbers =[1,2,3,4,5]
for item in numbers:
    print(item) # prints each item in a new line 
    
i=0
while i<len(numbers):
    print(numbers[i])
    i =i +1 # printseach item in a new line 
numbers.append(7) #adds 7 to the list 
numbers.insert(0,-1) #adds -1 at the beginning 
numbers.remove(3)
numbers.clear() #removes everything 
print(1 in numbers )# boolean
print(len(numbers))# retains number of elements in a list
print(numbers)
#range function
numbers =range(5)
print(numbers) #prints (0,5)

numbers = range(5,10,2) #prints numbers by adding 2 (10 is not included )
for number in range(5): # returns 0-4
    
#for number in numbers:
    print(number) # prints numbers in a list going down 
    
#tuples are not changeable
numbers(1,2,3,4)
numbers.count(3) #counts number of 3s

    
#use a comma to concatinate string and interger
# \n add a break or separates into different lines    
#.islower() =boolean
#name.lower() converts to lower case 
#len(name)  counts charecters
#name.index('i') gives you the postion of the letter i , e.g 1 on 'Tim'
#abs(-6) gives the absolute value of 6 
#max(4,5,9) prints highest number / min prints lowest 
#round(3.5) gives 4
#bin(3) converts to binary string 
# from math import *    print(sqrt(100))  to find the sqrt
#to use an input use variables 
name = input('input your name: ') #to input thename in the terminal 
name = input('Input your name: ')
age = input('Input your age :')
#print('Your name is : ' + name + 'and you are ' + age ' years old ')


sentence =input('Enter your sentence')
print('Your sentence is : '+sentence)
word1 =input('Enter the word to replace : ')
word2 =input('Enter the word to replace it with: ')
print(sentence.replace(word1,word2))

countries =['United Kingdom','Ghana','Nigeria','Australia'] #list can also be list(())
print(countries[2][0]) #prints N in Nigeria
print(countries[1:3]) #prints list from ghana to Nigeria
countries[2] ='New Zealand'
'''
'''
#list methods 
list1 =[1,2,3,4,5]
list2 =['banana','apples','mango','oranges']
list2.insert(1,'cherry') #inserts in the index 1
print(list2)
list2.remove('banana') #removes
list2.pop(1) #removes the value of the index stated on the list 
del list2[0] # deletes value of index 0 (del removes completely )
list2.clear() #delete all the values 
print(list2.index('mango')) #tells you where mango is located 
print(list2.count('mango')) #counts the number of mangos 
list1.sort() #prints in ascending order
list2.reverse() #reverses
list3 =list1.copy() # duplicate
list2.pop() #deletes last value

#tuples
three_numbers = (1,2,3)  #we can't change anything on the tuple unlike the list
print(three_numbers[1]) 
print(type(three_numbers[0]))
strings =('home','land','earth')
boo =(True,False,True)
three_numbers2 =tuple((1,'home',True)) #can print diff elements

#functions  indentation is very important -leads to invalid syntex
def greetings_function(name,age): #The parameter is telling the user which name it wants to greet name is a var
    print('Welcome '+ name + '.You are' +str(age) +'years old.') #remember to convert str or int
  
name=input('enter your name ')  #don't forget to use input in order to type in the terminal
age=input('enter your age')
    
greetings_function( name,age) #calling the function using the string John


#passing multiple vales in a tuple
def grreetings_function(*names):
    print('Welcome'+names)
    
grreetings_function('john','Tim','Tom')

#return statemets 
def add_numbers(num1,num2):
    return num1 + num2 # does not print functions after return statement 
num1 =int(input('Enter first number:'))
num2 =int(input('Enter second number')) #add the int function in order to add
print(add_numbers(num1,num2))

#if  else statements

a=2
b=3

if a>b:
    print(str(a) +'is greater than' +str(b))
    
if a == True: #boolean
    print('a is true')
    
if a == b:
    print('A equals B')
elif a>b:
    print('A is greater than B ')
elif b>a:
    print('B is greater than A')
else:
    print('A not equals to B')
    
#iN ORDER TO CHECK IF THER VALUE IS A STRING:
value =int(input('Input a value: ')) # add int because an input is recognised as str

if type(value)==str:
    print(value , 'is a string')
else:
    print(value ,'is not a string ') # add the comma when dealing with int to concanate
    
    
value =int(input('Enter a number: '))
 
if value%2==0:
    print('even number')
else:
    print('odd number') # this is to check if a number is odd or even
    
#dictionaries do not allow duplicates , you can't have 2 keys e.g (name,nationality) with the same name 
my_dict ={
    'name'       : 'Tim',
    'nationality': 'african',
    'Qualification': 'College'
}
x = my_dict['name']
print(x) #prints Tim
print(my_dict)['name'] #prints Tim
    
    
#while loops 
i =1
while i < 6:
      print(i)
      i += 1 # prints 1-5 going down

while i < 6 or i ==6:
    print(i)
    i += 1 #prints from 1-6 ""
    
#for loops 
for c in 'Mpho':
    print(c)  # prints Mpho going down 
    
#you can loop through a list
mylist = ['we' ,'are']
       
for values in mylist:
    print(mylist)
    if values =='we':
        break   #stops the loop
    
for x in range(4):
    print(x) #prints 0-4
else:
    print('Finished looping !!')
    
for x in range(3,7):
    print(x) #prints4-6
 
 
 #to do list 
my_list =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(my_list[1][1]) #prints 5 from the to do list

for lists in my_list:
    for row in lists:
        print(row) #nested loop loops from 1 to 9
        
#building a basic calculator 
num1 =int(input('Enter first number:'))
num2 =int(input('Enter second number:'))
op =input('Enter the operator:')

if op == '+':
    print('The addition is : ',num1+num2)
elif op == '-':
    print('The subtraction is : ',num1-num2)
elif op == '*':
    print('The multiplication is : ',num1*num2)
elif op == '/':
    print('The division is : ',num1/num2)
else:
    print('Invalid operator')
    
#Try except in python
try:
    x =int(input('Input an integer: '))
    print(x)
except ValueError:
    print('Value not an integer' ) #if you type in anything other than int
finally:
    print('try except finished') #it prints this whether ther is a problem or not
    
# open(countries.txt,'r') 'w' edit 'a' append the file 'r+' reading and writing in the file 

class Myclass:
    x =5
    
p1 =Myclass()
print(p1.x)  #prints 5 because p1=Myclas

class Person:
     pass #used to bypass errors to continue with the code
     def __init__(self,name,age):
        self.name=  name
        self.age =  age
name =input('Enter your name: ')  
age  =input('Enter your age:')      
p1 =Person(name,age)
print(p1.name) 
print(p1.age)

del p1.age
print(p1)

from new import Student

class Person(Student):
    pass

p1 = Person()
print(p1.name)  #prints the name Tim from the Student class in new 

#The python shell 
#open idle on your computer , works as a code editor
'''
#creating a simple login 
print('Create account now ')
username =input('Enter username: ')
password =input('Enter password: ')

print('Your account has been created successfully')
print('Login now!')

username1 =input('Enter username: ')
password1 =input('Enter password: ')
if username == username1 and password ==password1:
    print('You have loggen in successfully')
else:
    print('invalid credentials')
    
#modules in python 
def say_hi():
 print('Hi')
 #in another page 
import new #(the module for the file)

new.say_hi()
#pip  search for pypi for python modules
#django is a world-frame work that allows you to build websites using python


    


    
