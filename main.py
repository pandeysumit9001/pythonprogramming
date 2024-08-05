"""print("hello world")
print("this is my first program")
print(" i hope you all like it")"""
#two method to using multiple lines to print statement:
#tripple notation("""""")
#print("""hello world
#this is my first program
#i hope you all like it.""")
#/n-(blackslash)
#print("hello world \n this is sumit pandey \n i am going to learn data analytics with in a 2 months \n")
#single notation('')
#also used but its has a some drawbacks like-('it's has same cloth')this generate error

#comments in python
#two types of comments
#1-(#)used to singel line comment
#2-("""""")tripple line comment is used to multiple line comment

#creating variables

"""a="hello world"
print(a)"""

#data types in python

#user-inputs in python
#string
"""name=input("enter your name here: ")
print(name)"""
#integers
"""age=int(input("enter th e age of sumit: "))
print(age)"""
#floating numbers
"""length =float(input("enter the length of the person: "))
print(length)
"""
#evaluate
"""exp1=eval(input("enter any equation here: "))
print(exp1)"""

#typecasting and subtypes
"""name="sumit"
print(type(name))"""

"""age=int(input("enter the age: "))
print(type(age))"""
#implesit
"""a=123
b=1.23
print(type(a))
print(type(b))
c=a+b
print(c)
print(type(c))"""
#explesit
"""a="123"
print(type(a))
a=int(a)#as same as we write a code for float etc
print("after conversion",type(a))"""

#problems
#q1-
"""name="Sumit Pandey"
age=21
address="prayagraj"
print(name)
print(age)
print(address)"""
#q2-
"""num1=12
num2=13
temp=num1
num1=num2
num2=temp
print("the value of num1 is: ",num1)
print("the value of num2 is: ",num2)"""
#method..2
"""a=12
b=13
a,b=b,a
print(a)
print(b)"""
#q3-
"""num1=2.34
num1=int(num1)
print("after coversion",type(num1))"""
#q4-
"""name=input("enter the name of student: ")
grade=(input("enter the grade of student: "))
age=int(input("enter the age of student: "))
email=(input("enter the email of student: "))
phone=(input("enter the number of student: "))
print(":identity card of student:")
print(name)
print(grade)
print(age)
print(email)
print(phone)"""
#q5-
"""age=int(input("enter the age of sumit: "))
age=float(age)
print("after conversion",age)
print(type(age))"""

#operators
#Arithmetic operator
#+,-,*,%,/
#floor division(//)-it given after divide value which is not decimal value ,exponentiation(**)-2ki power 10
#comparison opearator
#>,<,=<,>=,==,!=
#logical opearator
#conditional statement
#if condition
"""marks = 97
if marks >= 95 :
    print("you will get a phone")
print("thanku ")"""

#if-else condition

"""marks = 86

if marks >= 89:
    print("you will get a phone")
else:
    print("you will not get a phone")
print("thanku")"""

#if elif else

"""marks=67
if marks>=90:
    print("goa trip")
elif marks>=80 and marks<=90:
    print("get phone")
elif marks>=70 and marks<=80:
    print("get book")
else:
    print("not get anything")"""

#nested statement

"""marks = 92
if marks>=80:
    print("get phone")
    if marks>=90:
        print("goa trip")

else:
    print("not get anything")"""

#short hand if statement

"""marks = 97
if marks >=90:print("get a phone")"""

#short hand if else statement

"""marks = 86
print("get a phone") if marks >= 90 else print("didnt get a phone")"""

#problem solving
#1 check no is positive or negative

"""num= int(input("enter the number:"))
if num>0:
    print("number is positive")
else:
    print("number is negative")"""

#2 number is odd or even

"""num = int(input("enter the number\n"))
if num%2==0:
    print("even")
else:
    print("odd")"""

"""marks=int((input("enter the num\n")))
print("even") if marks%2==0 else print("odd")"""

#3 area calculator
#square,rectangle,circle,triangle

#print("*****AREA CALCULATOR*****")
#print("press 1 to get the area of square
#press 2 to get the area of rectangle
#press 3 to get the area of circle
#press 4 to get the area of triangle")

"""choice=int(input("enter a number between 1-4: "))

if choice==1:
    side=float(input("enter a length of one side: "))
    area = side**2
    print("the are of square is ",area)
elif choice==2:
    length=float(input("enter a length of the rectangle: "))
    width=float(input("enter the width of the rectangle: "))
    area=length*width
    print("area of rectangle is: ",area)
elif choice==3:
    radius=float(input("enter a radius of the circle"))
    area=3.14*radius*radius
    print("area of circle is: ",area)
elif choice==4:
    base=float(input("enter a base of triangle: "))
    height=float(input("enter a height of triangle"))
    area=0.5*base*height
    print("area of triangle is: ",area)
else:
    print("please enter valid value")"""

#5 vowel or not

"""letter=input("enter a letter: ")
if (letter in "aeiou") or (letter in "AEIOU"):
    print("letter is vowel: ")
else:
    print("letter is consonent")"""

#6 check the number is single digit or 2 digit number and so on up to 5 digit

"""5=0-9
12=10-99
111=100-999
1111=1000-9999
11111=10000-99999"""

"""marks=int(input("enter a number\n"))

if marks>=0 and marks <= 9:
    print("it is single digit")
elif marks>=10 and marks <= 99:
    print("it is double digit")
elif marks >= 100 and marks <= 999:
    print("it is tripple digit")
elif marks >= 1000 and marks <= 9999:
    print("it is fourth digit")
else:
    print("it is fifth digit")
"""





