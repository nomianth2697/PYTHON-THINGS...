#                # STARTING CODING

# print("my name is nominath")
# #please don't remove this line
# '''dont do that mistakes'''
# '''this is a comment '''
# print('''hellow bhai mera naam nominath hai ,
# kya me aapka nam jan sakta hu?''')
# print('hellow')
# print ("hellow,world ")
# #my name is nominath
# print ("c:\'hellow")
# print ("nominath,\n is a good boy\t1")
# var1 = " nominath"
# print (var1)
# var4 =" house "
# print (var4)
# x1 = "vveee"
# x2 = 4
# x3 = 9.9
# print (x2+x3)
# print(type (x2))
# x5 = " boy"
# print(x1+x5)
# x4= "33"
# x6= "77"
# print (str(int(x4)+int(x6)))
# print(10* "infinix\n")



#                  # play with string

# mystr = ("Nominath kuwar is my name")
# print(mystr)
# #  to print any letter of string
# print(mystr[5])
# # to print 
# 
# 
# 
# 
# 
# h of the string
# print(len(mystr))
#  # if ve have specific segment, suppose we have first 8 letters
# print (mystr [0:8])
# # if we have to skip any letter of string
# print(mystr[0:12:2])
# # if we have to reverce the our streem
# print(mystr[::-1])
# # if we have to find index number of any list's item
# list1 = [1,5,5,2,3,4,6,7,8,9]
# print(list1.index(5))
# print(mystr[::-1])
# # if we have to check ends with "you have this name"
# print(mystr . endswith("name"))
# #if we have to count any wor ld or a name of our string
# print(mystr . count("n"))
# #if we haave to find any world or sentence of our string
# print(mystr . find("is"))
# # if we have to capatalize the first world
# print(mystr . capitalize())
# # if we have to string in upper case
# print(mystr . upper())
# # if we have to string in lowar case
# print(mystr . lower())
# # if we have to replace any world
# print(mystr . replace("is" , "A"))
# # if we have to new line in our string then use new line character ex. (\n)
# print("nominath \nis my name ")
# # if we have to single or double coat
# print("\"nominath\" is my name")
# # if we have to multiple words in print function
# print("hay",6,7,8)
# # if we have to seprate the values of a one print statement
# # if we have add any world to next print function then use end=""
# print("hay", 6,7, sep="~", end=("000\n"))
# print("nominath")
# #list
# list1 = [8,8.5,(4,5) , ("apple,banana")]
# print(list1)
# # dishnery
# disnery1 = {"name":"nominath", "age":18,"canVote": True}
# print(disnery1)
# # tuple
# tuple1 = [("parrot"," spraow ") , ("lion", "tiger")]
# print(tuple1)
# # if we have to code multiple line string
# apple ='''hii nominath ,
# i have to eat apple
# can you plz give me'''
# print(apple)
# print(len(apple))
# # if we have to print string on every single letter on new row
# for charactar in apple:
#     print(charactar)
#  # negative string slysing
# fruit =" mango"
# print(fruit[:-1])
# nm = "harry"
# print(len(nm))
# print (nm [-4:-2])
# Para= "Nursery rhymes, song lyrics, Dr. Seuss books — without realizing it," \
#       " we are surrounded by poetry every day. Poems can make children laugh," \
#       " but more than that, they can help with cognitive development"
# print(Para.lower())
# print(Para.upper())
# print(Para.find(","))
# print(Para.replace(",","."))
# print(len(Para))
# print(Para[:133])
# t= "nominath!!!!!!!!!!!!!!"
# print(t.rstrip("!"))
# #if we have to captaliz first letter
# print(t.capitalize())
# #if we have to print string in center
# print(t.center(50))
# print(len(t))
# print(Para.isupper())
# print(Para.islower())
# # if we have to check our string is alfanumeric(A-Z)(a-z)(0-9)
# print(Para.isalnum())
# print(mystr.isalpha())
# #if we have to check of our strings every word's starting
# # letter is capatal
# print(Para.istitle())
# #if we have to captailiz every word's first letter of our string
# print(Para.title())
# # if we have to convert upper case is lover and lover as upper
# print(Para.swapcase())

#   # taking input from user

# A = input("enter your name" )
# print("My name is ", A)

#                          # Calculater

# print ("enter your first number")
# n1= input()
# print ("enter your second number")
# n2= input()
# print("sum of these numbers " , int(n1) + int(n2) )



#     #TYPECASTING IN PYTHON

#  # The conversion of one data tupe into another data type is called typecastintg
# A=2.2
# B=2
# print(A+B)   #python self convert B into int to flot is callead indetermanate convertion


#                 # if ealse condision in python

# a=(int(input("enter your age")))
# print("Your age is",a)

# if (a<18):
#     print("You can not drive")
# else:
#     print("You can drive")

# # condisional opraters
# # (<),(>),(<=),(>=),(==),(!=)
# print(a<18)
# print(a>18)
# print(a<=18)
# print(a>=18)
# print(a==18)
# print(a!=18)

# appleprise= (int(input("enter todays apple prise")))
# bujet=100
# if(appleprise<=bujet):
#     print("You can buy Apple")
# else:
#     print("you can not buy apple please see another item")

# #if elif else
# num=int(input("enter the value of num"))
# if(num>0):
#     print("your value is +ve")
# elif(num==0):
#     print("your value is 0")
# else:
#     print("Your value is -ve")

# #Nested if statements
# num = int( input("enter num"))
# if (num < 0):
#     print("Number is negative.")
# elif (num > 0):
#     if (num <= 10):
#         print("Number is between 1-10")
#     elif (num > 10 and num <= 20):
#         print("Number is between 11-20")
#     else:
#         print("Number is greater than 20")
# else:
#     print("Number is zero")


#                     # Good morning sir
# # Please enter time in 24 hours clock format
# if (a<12):
#     print("Good morning sir")
#     print("Have a nice day")
# elif (a<16):
#     print("Good afternoon sir")
#     print("Have a nice day")
# elif (a<=20):
#     print("Good evening sir")
# elif (a > 25):
#     print("Enter the valid time")
# else:
#     print("Good night sir")
#     print("Good night")


#                 # loops in python

#                      # for loop

# Name = "Nominath"
# for i in Name:
#     print(i)
#     if (i=="i"):
#         print("hellow")

# list = ("santoor","lux","colegate","pen")
# for m in list:
#     print(m)
#     if (m=="lux"):
#         print("dont forget this is important")
#     for i in m:
#         print(i)
# # if we have the numvers from 1 to 100
# for k in range(1,100):
#     print(k)
#  # if we have in nagative
# for k in range(-10,0):
#     print(k)
# # if we have to skip any number of letter on the upper code then
# for k in range(1,100,2):
#     print(k)


#                     # while loobs

# i = 0
# while(i<=10):
#     print (i)
#     i=i+1
# # when we have decreasing order
# f=9
# while (f>-9):
#     print(f)
#     f=f-1
# # infinity loop
# # i=1
# # while(i>0):
# #     print (i)
# #     i=i
# # else in while loob
# n=9
# while(n>=0):
#     print(n)
#     n=n-1
# else:
#     print("sorry this condisition not matached")


#           # Brake and contanue statements

# for i in range (12):
#     print("5 X",i+1,"=",5*(i+1))
#     if (i==9):
#         break # breake means stop their

# for i in range(12):
#      if (i == 10):
#          print("skip the intreaction")
#          continue
#      print("5 X", i , "=", 5 * i)#Continue means skip this step

# i = 1
# while True:
#     print(i)
#     i=i+1
#     if (i==100):
#         break


#                         # function in pythom


# def calculategmean(a, b):
#     mean = (a * b) / (a + b)
#     print(mean)

# def calculateaddition(a, b):
#         addition = (a + b)
#         print(addition)

# def findgreatervalue(a,b):
#     if (a>b):
#         print("a is greater than b")
#     else:
#         print ("b is greater than a")

# # if we have to complate function letter
# def calculatesum(a,b):
#     pass #pass means we do this letter

# # we will add multiple values in our function
# # def avarage(a,b,c,d,e,f,g,h,i):
# #     print ("your ans is",(a+b+c+d+e+f+g+h)/8)

# a = 9
# b = 8
# gmean = (a*b)/(a+b)
# print (gmean)
#                         # or
# calculategmean(a,b)

# if (a>b):
#     print("a is greater than b")
#     calculategmean(a, b)
# else:
#     print ("b is greatar than a")
#     calculategmean(a, b)
#                     # or
# findgreatervalue(a,b)

# # c =33325
# # d = 5555424
# # print (c+d)
#                         # or
# # calculateaddition(c,d)

# # if we have to add multiple numbers in our function
# def findavarage (*numbers):

#     for i in numbers:
#         sum=0
#         sum = sum + i

#         print("your ans is",sum/len(numbers) )


# findavarage(5,6)


# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum+i
#         print("Average is: ", sum / len(numbers))
# average(5,6)


#                                # lists

# list1 = [5,6,7,5,8]
# print (list1)
# print (type(list1))
# print(list1[0])
# print(list1[1])
# print(list1[2])
# # negative indexing
# print (list1[-3])
# print(list1[len(list1) -3] )                 # this is all same
# print (list1[5-3])
# print(list1[2])
# # if we have to find in list1
# if 7 in list1:
#     print ('yes')
# else:
#     print("no")
# print (list1)
# print(list1[1:5])
# print(list1[1:5:2])
# # if we have to creat list on the go
# list2 = [i for i in range(19)]
# print(list2)
# print(list2 [10:12])


#                     # list oprations

# # if we have to add any letter in last of the list
# l = [5,44,8,1,1,2,5,78,66,6,7]
# print(l)
# # l.append(55)
# print (l)
# # if we have list in asending order
# # l.sort()
# print (l)
# # if we have list in desinding order
# # l.sort(reverse=True)
# print(l)
# # if we have to reverce the our list
# # l.reverse()
# print (l)
# print (l.index(78))
# # if we have to count any number how many times are repit in list
# print(l.count(1))
# m=l
# print (m)
# m[4]=69
# print (l)       # '''if we change in l it also change in m'''
# print (m)
#                     #then
# # if we copy the list
# n = l.copy()
# n[3]=45
# print (l)              #change only in n not in main list
# print (n)

# # if we have to insert any number in list
# l.insert(4,555555555)    #(index num. of list , number wich we have insert)
# print (l)
# # if we have to insert any other list in our list (in last)
# x = [10,100,1000]
# l.extend(x)
# print (l)
# # other way to insirt list in list
# z = [1,2,5,4,5,4,6,5,5,5,5]
# c = z+x
# print (c)


#                             # Tuple
#                 # we can not change tuple

# tup = (4,5,7,8,"Nominath","Hellow",True)
# print (type(tup),tup)
# print(len(tup))
# # if we not use , then one number of turple
# tup1 = (1) #this is int
# print(type(tup1))
# # if we use , in one number of turple
# tup2 = (1,) #this is turple
# print (type(tup2))
# # if we have to acess any word\number of tuple
# print (tup[1])
# print (tup[0])
# print (tup[5])
# if "Nominath" in tup:
#     print('Yes it has')
# else:
#     print ("Not in tup")
# # if we have to slysing with tuple
# tup3 = tup[0:5:2]
# print (tup3)

# print (type(tup3))
# print(tup[4:5])
# print (tup.index("Nominath"))

#                                 # F - strings
# # if we have to add any name or sentex on {} space
# letter = "hay my name is {} i am living in {}"
# name = "Nominath"
# country = "India"
# print (letter.format(name,country))
# # f-string
# print(f"hay my name is {name} i am living in {country}")
# prise= 1000.660211540
# txt="hay todays apple prise{}"
# # new way
# print(f"hay todays apple prise is {prise:.2f} rs.")
# # old way
# print(txt.format(prise))
# # if we have to show {}
# print(f"hay todays apple prise is {{prise:.2f}} rs.")


#                         # Doc-string
#                         # doc string not a comment
# '''this is a doc string'''
# def squere(a):
#     '''you have to put any number to squere '''
#     print(a**2)

# squere(5)
# # we can ascess doc-string
# print(squere.__doc__)           # we can ascess doc-string


#                             # Zen of python

# # if we acess to zen of pythom
# #     then print inport this into comond prompt


#                         # Recursion

# # if we have to find factorial
# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(3))
# print(factorial(4))
# print(factorial(5))


# # fibonacci squence
# def fibonaccisequence(n):
#     if (n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return (n-2)+(n-1)

# print(fibonaccisequence(2))
# print(fibonaccisequence(5))
# print(fibonaccisequence(500))
# print(fibonaccisequence(1))


#                         # Sets

# # not repeted value in sets
# S = {2,5,1,4,2,5,4}
# print(S) #set delete (2,4,5)
# # emty set is a dishnery
# Set = {0}
# print (type(Set))

# s1 = {1,2,5,6,4}
# s2 = {3,6,7}
# s3 = {11,22,33}
# # if we have to add sets
# print(s1.union(s2))
# # if we have to print all sets without any change
# print(s1,s2)
# # if we have to update s2's value in s1
# s1.update(s2,s3)
# print(s1,s2,s3)
# # 
# s1.intersection_update(s2)
# print(s2)
# # if we not have comon subject
# f1 ={'mango','orange','chiku'}
# f2 ={'pineapple','mango','chilli','orange','graps'}
# f3 = f1.symmetric_difference(f2)
# print(f3)
# f4 = f1.difference(f2)
# print(f4)


# # if we have to check there are values comon in all sets
# print (f1.isdisjoint(f2)) #means (isme koi aisa hai ki dono sets me aa raha hai)
# # False means hai
# # True means nahi hai

# # if we have ho add any in set
# f1.add("banana")
# f1.add("lichi")
# print(f1)
# # if we have to remove any in set
# f1.remove('chiku')
# print(f1)
# f1.discard("orange2") #diacard cannot throw errer
# print(f1)
# # if we have to select a random subjct from our set
# p1 = f1.pop()
# print(p1)
# # if we have to delete set
# f3= {11225}
# del f3



#                             # Dictionaries

# dict={
#     'name':"nominath",
#     'age': 18,
#     'standred':'bsc fy',
#     'collage':'dagdujirao'}
# # if we have to acess distnury
# # in there name is key    and      nominath is value
# print(dict.get('name'))             #this type cannot throw error
#                         # or
# print(dict['name'])
# print(dict['age'])
# print(dict['collage'])
# print(type(dict))
# # if we have all keys of dictenory
# print(dict.keys())
# # if we have all values of dictenry
# print(dict.values())
# # if we have all values of keysk
# #             or
# for key in dict.keys():
#     print(dict[key])
# # if we have key value pairs
# print(dict.items())

# # upgrade in dishneuri
# ep1 = {122:45 ,123:89, 567:69 ,678:69}
# ep2 = {222:67 , 566:98}
# # if we have to add ep2 in ep1
# ep1.update(ep2)
# print (ep1.keys())
# print(ep1.items())
# print(ep1.values())
# # if we have to cleare any distnery
# ep2.clear()
# print (type(ep2))
# # if we have to clear any key and value pair from dish
# ep1.pop(122)
# print(ep1)
# # if we have to clear last key value pair of dist
# ep1.popitem()
# print(ep1)
# ep3={122:45,566:98}
# ep1.update(ep3)
# print (ep1)
# del ep2


#                             # for loobs with else

# for n in range(10):
#     print (n)
#     # if (n == 8):
#     #     break

# else:
#     print('sorry')


#                           # ERROR HANDLING
# # try and exception
# a = input('enter the number')
# print(f"multiplation table of {a} is:")
# try:
#     for i in range(1, 11):
#         print(f"{int(a)}X{i} = {int(a) * i}")
# except Exception as e:
#     print (e)

# # finaly
# # finally is always exucated
# def funk1():
#     try:
#         l = [1, 5, 6, 7]
#         i = int(input("enter the index"))
#         print(l[i])
#         return 1
#     except:
#         print("Invalid index")
#         return 0
#     finally:
#         print("i am always exucared")


#                                  # custam error
# # if we have to rease custon error
# v = int(input("enter the value between 4 to 10  :  "))
# if (v<4 or v>10):
#     raise SyntaxError('you enter invalid senterx')


# a = input("enter the value")

# if (a=='quit'):
#    print(' you enter quit')
# elif(int(a)<(4) or int(a)>(10) ):
#    raise ValueError('invalid input')


#                         # SHORT HAND IF EALSE

# a= 33225
# b = 44454
# print("A") if a>b else print("=") if a==b else print("B")

# c=6 if a>b else"sorry"
# print(c)


#                             # enumerate function in python

# marks = [25,15,45,88,77,45,65,85,99]

# index = 0
# for mark in marks:
#     print(mark)
#     index = index+1
#     if (index == 3):
#         print("nomi")
# #             or
# for index,mark in enumerate(marks,start=1):
#     print(mark)
#     if (index==3):
#         print("nomi")


#                             #  import function in python

# # if we have to import any function
# import pandas
# # if we have to name function in short
# import pandas as pd
# # if we have to find how many function there is an pandas
# print(dir(pandas))
# # we can also create our program and import it


# #                    lokal and global beriable
# # we can use global veriable in function
# # we can not use lokal veriable in outside

# x=10 # x is a global number
# print(x)
# def my_function():
#     y=5 # y is lokal number
#     print(y)
#     global x # we can change global x with the help of global function
#     x = 8
#     print(x)
# my_function()
# print(x)
# # print(y) # there are y is lokal number we can not print it

#                             # file os

# # if we have to read then 'r', for write 'w', for append 'a'.
# f = open('bbb.txt','r')
# # if we have to find what is the text in the file
# text = f.read()
# print(text)
# # if we have to create a file and write any content in new file
# c = open("created.txt","w")
# c.write('Hay i am a sudent who are preapring for data science.')
# # if we have to find length of write
# # print(write)
# # if we have to write any sentex in our exesting file.
# with open ('bbb.txt','a'):
#     c.write('\nhellow')
# c.close()

# # read lines()
# f = open('myfile.txt', 'r')
# i = 0
# while True:
#   i = i + 1\
  
#   line = f.readline()
#   if not line:
#     break
#   m1 = int(line.split(",")[0])
#   m2 = int(line.split(",")[1])
#   m3 = int(line.split(",")[2])
#   print(f"Marks of student {i} in Maths is: {m1*2}")
#   print(f"Marks of student {i} in English is: {m2*2}")
#   print(f"Marks of student {i} in SST is: {m3*2}")

#   print(line)

# # write lines()
# f = open('myfile2.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()

# with open ('file.txt',"r") as f:
#   print(type(f))
# # if we have to read any text file from specific lenth
#   f.seek(10) # he was reading text file with 10 number
#   # if we have to read to specific lenth
#   c = f.read(16)
#   print(c)
#   # if we have to find where from seek()
#   print(f.tell())

# with open('sample.txt',"w") as f:
#   f.write("hellow world!")
#   # if we have write to specific length
#   f.truncate(5)

# with open('sample.txt') as f :
#   data = f.read()
#   print(data)


#                 # lambda functions in python

# def double(n):
#   return n*2
# print(double(5))
# # using lambda function
# double = lambda n:n*2
# print(double(5))

# avg = lambda x,y,z: (x+y+z)/3
# print (avg(3,5,10))

# dev = lambda n:n/2
# add = lambda a:a+6
# sub = lambda b:b-(7)
# into = lambda g:g*g
# cube = lambda x :x*x*x

# print(dev(65))
# print(add(457))
# print(sub(475518))
# print(into(665))
# print(cube(5))
# def find(a,b):
#     return (a)(b)

# print(find(add,5))

# # ve can use function in function
# def appl(s,d):
#   return 6+s(d)
# print(appl(cube,2))


#                         # map, filter and reduce

# # map
# def cube(n):
#     return n*n*n
# print(cube(2))

# l = [1,2,3,4,5,6,7]
# newl = []
# for item in l:
#     newl.append(cube(item))
#                                     # or
# newl = list(map(cube,l))
# print(newl)

# # filter
# def filter_function (a):
#     return a>4
# # if we have to check any number is grater than 4
# print(filter_function(5))

#                                   #  or
# # if we have object is greter then 4
# new1 = list(filter(filter_function,l))
# print(new1)                
# filter

# from functools import reduce
# def sum (x,y):
#     return(x+y)

# aditya = reduce (sum,l)
# print(aditya)


#                             # is and (==)

# a = 4
# b = 4
# print(a is b) # location of object (only one object)
# print(a==b)  # value   (same) 

# x = [1,4,34]
# y = [1,4,34]

# print(x is y)
# print(x==y)

# x = (1,4,34)
# y = (1,4,34)

# print(x is y)
# print(x==y)

#                             # Oops in python

# # classes and object

# class Person:
#     name = "Nominath"
#     accupation = "Data Scientist"
#     networth = "1000 dollar"
#     at = "Munbai"
#     familymembers = 5

# a = Person
# print(a.name)
# # if we have to change data
# a.name = "Aditya"
# a.accupation = "Police"
# print(a.name,a.accupation)
# print(type(a))
# def info(self):
#     print(f"{self.name} is a {self.accupation} at {self.at}")

# info(a)
# b = Person()
# b.name = "Nominath"
# b.accupation = "Data Scientist"
# b.at = "Dubai"
# info(b)

# c = Person()
# # if we not enter the value then it will take defolt
# info(c)
# c.name = 'Moti'
# c.accupation = "dog"
# c.at = "my house"
# info(c)

#                        #  constractars in python

# class person():
#     def __init__(self,n,o):

#         self.name = n
#         self.occ = o
        
# def info(self):
#     print(f"{self.name} is a {self.occ}")

# a = person("Nominath","Data Scientist")
# b = person("moti","dog")
# info(a)
# info(b)


#                     # DECORETERS in python
# # modifieng the function
# def hellow():
#     print("hellow world")

# def greet (fx):
#         def mfx():
#             print("Good Morning")
#             fx()
#             print("thanks for using this function")
#         return mfx
# @greet
# def hellow():
#     print("hellw world")

# hellow()

# def hellow():
#     print("hellw world")
# def add(a,b):
#     print(a+b)
# hellow()
# def hellow():
#     print("hellow world")

# def greet (fx):
#     def mfx(*args,**kwargs):
#         print("Good Morning")
#         fx(*args,**kwargs)
#         print("thanks for using this function")
#     return mfx
# @greet
# def add(a,b):
#     print(a+b)
# add(1,2)
# # greet(add)(5,5)

#                       # Gatters and setters in python
#                     #   day 60

# class myclass:
#     def __init__(self,value):
#         self._value = value
#     def show(self):
#         print(f"value is {self._value}")

# # how to create a gratter
# # @property is use to create gratter
# # we can not change gratter
#     @property 
#     def ten_value(self):
#         return 10*self._value

# # How to create setter
#     @ten_value.setter
#     def ten_value(self,new_value):
#         self._value =new_value/10

# obj = myclass(10)
# obj.ten_value=67
# print(obj.ten_value)
# obj.show()
# # we can not change gratter
# # obj.ten_value = 58

#                         #61
# class Employee:
#     def __init__(self,name,id) :
#         self.name = name
#         self.id = id
    
#     def show(self):
#         print(f"the Employee: {self.id} is {self.name}")

# # if we have to create new class with the helf of old class

# class Programmer(Employee):
#     def lan(self):
#         print ("the defolt launguge is python \nbut you can learn other laungauge")

# rajesh = Employee("rajesh",420)
# rajesh.show()
# ram =Employee("ram",1001)
# ram .show()
# nomi = Programmer("nominath",1)
# nomi.lan()
# moti= Programmer("moti",45)
# moti.show()
# moti.lan()


# # public attribute

# class workman:
#     def __init__(self):
#         self.name = "nominath"
#         self.age = 18

# a = workman()
# print(a.name)


# # Private attribute

# # if we have to privet any function 
# # there ve priveting name with help of __name
# class employee:
#     def __init__(self):
#         self.__name = "nominath"
#         self.__age = 18
# # we cannot acess name with this type
# # a = employee()
# # print(a.__name)
# # if we have to acess __name
# # print(a.(_name of class)(attribute))
# a = employee()
# print(a._employee__name)
# print(a.__dir__())

#                         #  static methods
# a
# class math:
#     def __init__(self,num) :
#         self.num = num
    
#     def addtonum(self,n):
#         self.num = self.num + n
    
#     # @staticmethod
#     def add(a,b):
#         return a+b


# a = math(5)
# print(a.num)
# a.addtonum(6)
# print(a.num)
# print(math.add(1,2))

#                                 # class veriable vs instance veriable

# class employee:
#     companeyname="Apple"
#     def __init__(self,name):
#         self.name = name
#         self.salary = "5500k"

#     def showdetails(self):
#         print(f"the name of componey is {self.companeyname} employee is {self.name} and the salary of employee is {self.salary}")

# a1 = employee("moti")
# a1.salary = '600k'
# a1.companeyname = "microsoft"
# a1.showdetails()
# a2 = employee('nominath')
# a2.showdetails()

# class employee:
#     companey = "apple"
#     def show(self):
#         print(f"the name is {self.name} and companey is {self.companey}")
#     # @classmethod     
#     def changecompaney (cls,newcompaney):
#         cls.companey = newcompaney

# e1 = employee()   
# e1.name = "Nomi" 
# e1.show()   
# e1.changecompaney("Tesla")
# e1.show()   
# print(employee.companey)

# class employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

# # whaen our data in string

#     @classmethod
#     def fromstr (cls,string):
#         return cls(string.split("-")[0],string.split("-")[1])

# a = employee("nominath",120000)
# print(a.name)
# print(a.salary)

# string = "aditya-120000"
# b= employee.fromstr(string)
# print(b.name)
# print(b.salary)


# # dir dict or help in python

# # dir
# a =[1,2,3]
# print(type(a))
# print(dir(a))

# # __dict__
# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.version = 1

# p = person("nomi",18)  
# print(p.__dict__)

# # help
# print(help(p))


# # super keyword in python

# class perentclass:
#     def perent_method(self):
#         print("this is the perent class")

# class childclass(perentclass):
#     def perent_method(self):
#         print("nominath")
#         super().perent_method()
#     def child_method(self):
#         print("this is a child class")
#         super().perent_method()

# child_object = childclass()
# child_object.child_method()
# child_object.perent_method()

# class emplyoee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
# class programer(emplyoee):
#     def __init__(self, name, id,lang):
#         super().__init__(name,id)
#         self.lang = lang

# rohan = emplyoee("rohan das",420)
# nominath = programer("nominath kuwar",1120,"python")
# print(nominath.name)
# print(nominath.id)
# print(nominath.lang)


# # magic/dunder methods in python
# # (__method__)

# from emp import employee

# e = employee("nominath")
# # print (e.name)
# # print(len(e))
# print(str(e))
# print(repr(e))


# # method overweiting

# class shape:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def area(self):
#         return self.x * self.y

# # rec = shape()
# # # print(rec.area())

# class circle(shape):
#     def __init__(self, redi):
#         self.redi = redi
#         super().__init__(redi,redi)

#     def area(self):
#         return 3.14 * super().area()

# c = circle(3)


# class vector:
#     def __init__(self,i,j,k):
#         self.i = i 
#         self.j = j 
#         self.k = k 

#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"

#     def __add__(self,x):
#         return vector(self.i + x.i,self.j + x.j,self.k + x.k)

# v = vector(3,4,5)
# print(v)
# v1 = vector(2,5,4)
# print(v1)
# print(v+v1)
# print(type(v+v1))


#                             # inheritances in python


# # single inheritance

# class animal:
#     def __init__(self,name,species):
#         self.name = name
#         self.species = species

#     def make_sound(self):
#         print("sound made by animal")

# class dog(animal):
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#     def make_sound(self):
#         print("Bark!")

# d = dog("moti","street")
# d.make_sound()
# a = animal("tiger","bengol")
# a.make_sound()

# # Quik Quiz
# class cat(animal):
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type

#     def size_of_nail(self):
#         return "size of nail of cat"
#     def hight(self):
#         print(f"hight of cat")


# # multipal inheritance

# class employee:
#     def __inti__(self,name):
#         self.name = name
#     def show(self):
#         print(f"the name of employee is {self.name}")
        

# class dancer:
#     def __init__(self,dance) :
#         self.dance = dance
#     def show(self):
#         print(f"the name of dance dance is {self.dance}")

# class Dancer_Employee(employee,dancer):
#     def __init__(self,name,dance):
#         self.dance = dance 
#         self.name = name
         
       

# a = Dancer_Employee("Nominath","HipHop")
# print(a)
# print(a.name)
# print(a.dance)
# a.show()
# print(Dancer_Employee.mro())


# # multi-level inheritance 

# class Animal: 
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Species: {self.species}")
        
# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def show_details(self):
#         Animal.show_details(self)
#         print(f"Breed: {self.breed}")
        
# class GoldenRetriever(Dog):
#     def __init__(self, name, color):
#         Dog.__init__(self, name, breed="Golden Retriever")
#         self.color = color
        
#     def show_details(self):
#         Dog.show_details(self)
#         print(f"Color: {self.color}")

# o = GoldenRetriever("moti","golden and white")
# o.show_details()
# print(GoldenRetriever.mro())


# # hybreed inhiretance

# class Baseclass:
#     pass
# class derive1(Baseclass):
#     pass
# class derive2(Baseclass):
#     pass
# class derive3(derive1,derive2):
#     pass


# # hierarchical inheritance

# class manager :
#     pass 
# class e1(manager):
#     pass 
# class e2(manager):
#     pass
# class e3(manager):
#     pass
# class e4(e1):
#     pass



# # time module in python

# import time

# def usingwhile():
#     i = 0
#     while i<50000:
#         i = i+1
#         print(i)


# def usingfor():
#     for i in range(50000):
#         print(i)

# init = time.time()
# usingwhile()
# t1 =time.time()-init
# init = time.time()
# usingfor()
# print(t1)
# print(time.time()-init)


# # walrus oprater

# a = True
# print(a)
# print(a:=False)

# numbers = [1,2,3,4,5]

# while(n:=len(numbers)) >0:
#     print(numbers.pop())
# print(len(numbers))

# foods = list()

# while True:
#     food = input("what food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)
#     print(foods,len(foods))

# foods = list()
# while(food:= input("what food do you like?: "))!="quit":
#     foods.append(food)
# print(foods,f"there is {len(foods)} foods in your list")


# # shutil module in python

# import shutil
# import os

# # shutil.copy("hellow","myhellow")

# # shutil.copytree("hellow","welcome")
# # shutil.move("pyvenv.cfg","venv/pyvenv.cfg")
# # os.Fpi("myfile.txt")# if we have to delete any file



# response = requests.get ("https://www.w3schools.com/python/module_requests.asp")  
# print(response.text)
# print(response.status_code)

# url = "https;//www.codewitharry.com"
# data = {
#     "massage":'hellow'
#     "bye" 
# }

# requests.post(url=url,data=data)


# # function cashing

# from functools import lru_cache
# import time

# @lru_cache(maxsize=None) 

# def fx (n):
#     time.sleep(5)
#     return n*5

# print(fx(20))
# print("done for 20")
# print(fx(40))
# print("done for 40")
# print(fx(36))
# print("done for 36")
# print(fx(8))
# print("done for 8")

# print(fx(20))
# print("done for 20")
# print(fx(40))
# print("done for 40")
# print(fx(36))
# print("done for 36")
# print(fx(8))
# print("done for 8")
# print(fx(61))
# print("done for 61")


# # regular expractions in python

# import re

# pattern = "was"
# text = '''The Waddesdon Bequest was left to the British Museum in 1898 by Baron Ferdinand Rothschild's will. Taken from his New Smoking Room at Waddesdon Manor, it consists of almost 300 pieces, including jewellery, plate, enamel, carvings, glass and maiolica. Earlier than most objects is the Holy Thorn Reliquary, probably created in the 1390s in Paris for John, Duke of Berry. The wide-ranging collection is in the tradition of a treasure house, such as those owned by the Renaissance'''

# surch = re.search(pattern,text)
# print(surch)


# # asyncIO in python

# import time
# import asyncio
# import requests

# async def function1():
#     print('func1')
#     url = "https://images.app.goo.gl/W7WyzS8TaekqyshD8"
#     responce = requests.get(url)
#     open("4k.jpg", "wb").write(responce.content)
#     return "nominath"

# async def function2():
#     print('func2')
#     url = "https://images.app.goo.gl/qxXk7SVifTbGeCLP7"
#     responce = requests.get(url)
#     open("4k2.docx", "wb").write(responce.content)

# async def function3():
#     print('func3')
#     url = "https://images.app.goo.gl/xXx8myVSCp4rEbreA"
#     responce = requests.get(url)
#     open("4k3.pdf", "wb").write(responce.content)
    
    
# async def main():
#     l = await asyncio.gather(
#         function1(),
#         function2(),
#         function3(),
#     )
#     # # print(l)
#     # # task = asyncio.create_task(function1())
#     # await function1()
#     # await function2()
#     # await function3()

# asyncio.run(main())




# async def v1():
#     time.sleep(3)
#     return "hellow world"

# async def v2():
#     time.sleep(3)
#     return "hellow world"

# async def v3():
#     time.sleep(3)
#     return "hellow world"
# async def main():
#     l = await asyncio.gather(
#         v1(),
#         v2(),
#         v3(),)
#     print(l)

# asyncio.run(main())
print("hellow world ")

#                     # multitherding in python

# import threading
# import time

# def func(seconds):
#     print(f"sleepig for {seconds}seconds")
#     time.sleep(seconds)

# # time1 = time.perf_counter()
# # # normal code
# # func(4)
# # func(2)
# # func(1)
# # time2 = time.perf_counter()
# # print(time1-time2)

# # # code using threading
# t1 = threading.Thread(target=func,args=[4])
# t2 = threading.Thread(target=func,args=[2])
# t3 = threading.Thread(target=func,args=[1])
# time1 = time.perf_counter()
# t1.start()
# t2.start()
# t3.start()
# # if we have to wait our program will end
# t1.join()
# t2.join()
# t3.join()


# time2 = time.perf_counter()
# print(time1-time2)


# import multiprocessing
# import requests

# def downloadFile(url,name):
#     print(f"started downlode{name}")
#     responce = requests.get(url)
#     open(f"file{name}.jpg", "wb").write(responce.content)
#     print(f"finished downloding{name}")

# if __name__=="__main__":

#     url = "https://picsum.photos/200/300"
#     pros =[]
#     for i in range(50):
#         # downlodeformurl(url,i)
#         p = multiprocessing.Process(target=downloadFile, args=[url, i])
#         p.start()
#         pros.append(p)
        
                                                                                                                                                                                                                                                                                                                    # for p in pros:
                                                                                                                                                                                                                                                                                                                    #     p.join()


#                                 # ENDIG PYTHON COURCE #


# # print("hellow world")
# import pyaudio as pa
# import speech_recognition as s_r
# print(s_r.__version__)
# r = s_r.Recognizer()
# my_mic = s_r.Microphone(device_index=1)

# a= input("what is your favourate superhero?\n ")
# print(f"{a} is my favourate superhero!")

# for i in range(7000):
#     print(i+1)  

#     while (i==9):
#         print("print hellow wor
# a = list(1)







# class Solution(object):
#     def findWordsContaining(self, words, x):
#         ans = []
#         for i, word in enumerate(words):
#             if x in word:
#                 ans.append(i)
#         return ans
        
a = int(input("enter the number"
              ))  
b = int(input("enter the number"))  
c = int(input("enter the number"))  
print(a)      
print(b)      
print(c)      
        