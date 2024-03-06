# Krishta Software

lst = [4, 6, 2, 7, 1, 5]


# lst2 = [-1, 2, 9, -5]
# lst3 = ['a', 1, 2, -3]
# lst4 = [2.3, 6, -1.5, 11]
# lst5 = [0, 4, 'hf dk', 5, 6]
# lst6 = [False, 1, -7, 6, 7]
# lst7 = [(1, 2, 3), 5, 6, 9]
# lst8 = [[1, 2], 5, 6, 11]
# lst9 = [{1: 11, 'a': 'abc'}, 4, -4, 0, 6]


def multi(li):
    minimum = li[0]
    new_list_empty = []

    for i in lst:
        if i == minimum:
            continue
        else:
            if i < minimum:
                minimum = li[i]
                new_list_empty = new_list_empty.append(minimum)
                new_list_empty = li.remove(minimum)

    print(f'new_list is {new_list_empty}')


li = [4, 6, 2, 7, 1, 5]
multi(li)
# ****************************************************************

# Infobeans

# Online Python compiler (interpreter) to run Python online.

# print("Hello world")
import re

# first = [1, 2, 3, 4, 5]
# second = first
# second.append(6)
# print(first)
# print(second)

# list = [1,0,9,0,1,5,6,9,8,0,0,1,5]
# emplist1 = []
# # emplist2 = []
# for i in list:
#     if i!=0:
#         emplist1.append(i)

#     if i==0:
#         emplist2.append(i)

# print(emplist1)
# print(emplist2)
# for i in emplist2

x = ['a', 'bc', 'def']

if len(x) >= len(x):
    z = len(x)
    print(z)
print(z)

# line no.65

# string = ['a', 'bc', 'def']
# longest = len(max(re.findall(r'\S+', string), key=len))
# print(longest)

# values = ['a', 'bc', 'def']
# current_max = 0
# for v in values:
#     if v > current_max:
#         current_max = v

string = "My name is kolhapur"
string = string.split()
max_word = ''
for word in string:
    if len(word) > len(max_word):
        max_word = word

print(max_word)  # kolhapur


def long_word(s):
    n = max(s.split())
    return (n)


str2 = 'a bb ccc dddd'
print(long_word(str2))

string = "Hello I like cookies"
string3 = re.findall(r'\S+', string)
print(string3)  # ['Hello', 'I', 'like', 'cookies']
maxlen = max(len(word) for word in string3)
print(maxlen)  # 7
# ------------------------------------------------

# Given string in that we have to remove numerical value

output = re.sub(r'\d+', ' ', '123hello 456world')
print(output)  # 'hello world'
# ------------------------------------------------

# In the given string we have to remove only alphabets
string77 = "Hello I23 like56 7cookies"
lst7 = []
for i in string77:
    if i.isdigit():
        lst7.append(i)
print(lst7)  # ['2', '3', '5', '6', '7']
lst9 = ''.join(lst7)
print(lst9)
print(type(lst9))

result = re.sub(r'\D', '', 'zsd67637 9d')
print(result)  # 676379

result2 = re.sub("[^0-9]", "", "sdkjh987978asd098as0980a98sd")
print(result2)  # 987978098098098
# ------------------------------------------------
# How to convert list into the dictionary

myList = ['a', 'apple', 'b', 'banana', 'c', 'cherry']

myDict = {myList[i]: myList[i + 1] for i in range(0, len(myList), 2)}
print(f'First solution is, {myDict}')
# {'a': 'apple', 'b': 'banana', 'c': 'cherry'}

for i in range(0, len(myList), 2):
    myList[i]: myList[i + 1]
print(f'Second solution is, {myDict}')

listKeys = ['a', 'b', 'c']
listValues = ['apple', 'banana', 'cherry']

myDict = {listKeys[i]: listValues[i] for i in range(0, len(listKeys), 1)}
print(f'Third solution is, {myDict}')
# {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
# ------------------------------------------------

print(sorted([5, 2, 3, 1, 4]))  # [1, 2, 3, 4, 5]

a = [5, 2, 3, 1, 4]
a.sort()
print(a)  # [1, 2, 3, 4, 5]


# ------------------------------------------------
# Write a Program for Sum of squares of first n numbers

def sumsq(n):
    summ = 0
    for i in range(1, n + 1):
        summ += i * i

    return summ


print(sumsq(3))
# ------------------------------------------------
# Find out second largest number from list

list1 = [10, 20, 4, 45, 99]
new_list = set(list1)
new_list.remove(max(new_list))
print(max(new_list))

list1 = [10, 20, 4, 45, 99]
print("Second largest element is:", sorted(list1)[-2])

lst = [10, 20, 4, 45, 99]
m = max(lst)
x = [a for i, a in enumerate(lst) if a < m]
print(max(x))
# ------------------------------------------------
sample = 'abndceghkjdkdh'
output = 'adgj'

# sample = [::3] ?
# ---------------------------------------------------
# Data Axle
# LOCUST Python Performance tool


dict1 = {1: 'a', 2: 'b', 4: 'z', 3: 'g', 7: 'as'}
# var = sorted(dict1)
# print(var)

# dict2 = {}
# for k, v in dict1.items():
#     for i in var:
#         if k == dict2[i]:
#             dict2[i] = dict2.get(i, dict1[v]) ???????????????

#     print(dict2)
for k, v in sorted(dict1.items()):
    print(k, ':', v)
# ----------------------------------------------------------
string1 = "A@nk!T&@123"
str2 = ''
for indec, i in enumerate(string1):

    if i.isalnum():
        str2 = str2 + i
    else:
        str2 = str2 + i

print(str2)
print(str2[::-1])
# ----------------------------------------------------------
# Test_file2
# Agiliad Technology

a = [[[[[[6]]]]]]

while a is not list:
    try:
        a = a.pop()
    except:
        print(a)
        break
# -----------------------------------------
a = 'Zunjhar'
print(a[:-1])  # Zunjha
print(a[1:])  # unjhar
print(a[-1:])  # r
print(a[::-1])  # rahjnuZ
print(a[::-2])  # rhnZ

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
print('A0 = ', A0)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

A1 = range(10)
print('A1 = ', A1)
# [0,1,2,3,4,5,6,7,8,9]

A2 = sorted([i for i in A1 if i in A0])
print('A2 = ', A2)
# []

A3 = sorted([A0[s] for s in A0])
print('A3 = ', A3)
# [1, 2, 3, 4, 5]

A4 = [i for i in A1 if i in A3]
print('A4 = ', A4)
# [1, 2, 3, 4, 5]

A5 = {i: i * i for i in A1}
print('A5 = ', A5)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

A6 = [[i, i * i] for i in A1]
print('A6 = ', A6)
# [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
# -----------------------------------------
# Test_File

str = 'My Programming language is Python'
# str = list[str]
lst = {}

for i in str:
    lst[i] = lst.get(i, 0) + 1
    print(lst[i])
print(lst)
# count = str.count(i)
# # print(i, 'occured', count)
# if count >= 2:
#     lst = lst.append(i)
#     print(lst)

# Brijesh sahu : Auther

# -----------------------------------------
# String_operations
stringz = "How are you"
count = {}
for i in stringz:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1
print(count)
# {'H': 1, 'o': 2, 'w': 1, ' ': 2, 'a': 1, 'r': 1, 'e': 1, 'y': 1, 'u': 1}
# ------------------------------------

list = ["google", "apple", "msft"]


# list2 = str(list)
# print(type(list2))
# print(list2)
def is_isogram(list3):
    for ch in list3:
        # print(ch)
        if list3.count(ch) > 1:
            # print(ch)
            return False
    return True


# print(is_isogram(list))
print(is_isogram('abcd'))
print(is_isogram('apple'))
# anagram
# ------------------------------------

# Count each character from string

str2 = 'www.zZ Zunjarr.com'
d = {}

for i in str2:
    d[i] = d.get(i, 0) + 1

print(d)
# ------------------------------------

from collections import Counter

str3 = 'www.zZ Zunjarr.com'
out = Counter(str3)
print(out)
print(out.items())
# ------------------------------------
# Palindrome

str4 = 'madam'
if str4 == str4[::-1]:
    print(True)
else:
    print(False)
# ------------------------------------

# You can use max on the splitted string with key as len:

string2 = 'My name is Zunjarr'
max_word = max(string2.split(), key=len)
print('longest word in a string is: ', max_word)

# Using loop :
string = input("Enter a string ")

max_word = ''
for word in string.split():
    if len(word) > len(max_word):
        max_word = word

print(max_word)
# ------------------------------------
# Star_pattern
for i in range(5):
    print(' ' * (5 - i), '*' * i)
#    *
#   **
#  ***
# ****
# -------------------------------------
print('New program \n')

for i in range(4):
    print(' ' * i, '*' * (4 - i))
# *****
#  ****
#   ***
#    **
#     *
# -------------------------------------
print('Next program \n')

for i in range(5):
    print('*' * i, ' ' * (5 - i))
# *
# **
# ***
# ****
# -------------------------------------
print('Next level program \n')

for i in range(5):
    print('*' * (5 - i), ' ' * i)

# *****
# ****
# ***
# **
# *
# -------------------------------------
print('Number pattern \n')

rows = 5

for row in range(1, rows + 1):  # 1, 2, 3, 4, 5
    for column in range(1, row + 1):  # 1
        print(column, end=' ')

    print('')

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# -------------------------------------
rows = 5

for row in range(1, rows + 1):  # 1, 2, 3, 4, 5
    for column in range(1, row + 1):  # 1
        print(row, end=' ')

    print('')

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# -------------------------------------
# --------------------------------
from datetime import datetime

# now = datetime.now().strftime("%H:%M:%S")
# print(now)

now = datetime.now()
current_time3 = now.strftime("%H:%M:%S")
print("Current Time =", current_time3)
# --------------------------------
import time

t = time.localtime()
current_time2 = time.strftime("%H:%M:%S", t)
print(current_time2)

current_time = time.ctime()
print(current_time)
# --------------------------------
strg = 'w45&*67jh'

for i in strg:
    if i.isalnum:
        print('Its alphanumeric')
    else:
        print('Not')

import re

text = '12qw$%'
if re.match(r'^[A-Za-z0-9_]+$', text):
    print('Its alphanumeric text')
# --------------------------------

# Sample_test
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist2 = ["apple", "banana", "cherry"]
tropical2 = ["mango", "pineapple", "papaya"]
thislist2.append(tropical)
print(thislist2)
# ['apple', 'banana', 'cherry', ['mango', 'pineapple', 'papaya']]


str1 = {"abc", "123", }  # set
print(type(str1))
str2 = {"abc", "123"}  # set
print(type(str2))


# -------------------------------------------------
# Inheritance

class A:
    def method1(self):
        print("inside method 1")

    def method2(self):
        print("inside method 2")


class B(A):
    def method3(self):
        print("inside method 3")

    def method4(self):
        print("inside method 4")


a = A()
a.method1()
a.method2()
b = B()
b.method3()
b.method4()
b.method1()
b.method2()
# -------------------------------------------------
# Abstract Method

from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("Method of Laptop class is invoked")


# c = Computer()      # TypeError: Can't instantiate abstract class Computer with abstract method process
# c.process()
l = Laptop()
l.process()
# -------------------------------------------------
# Input : [5, 4, 6, 0, 5]
# Output : 20

lst = [5, 4, 6, 0, 5]
summ = 0
for i in lst:
    summ = i + summ
print(summ)
# -------------------------------------------------

Sample = [1, 2, 4, 5, 2, 3, 2, 6, 2, 7]
# Expected Output : element = 2, count = 4

empty_list = []
count = 0

for count, item in enumerate(Sample):
    print("Animal number", count, "in the list is", item)

for i in Sample:
    if i in empty_list:
        count = count + 1
    else:
        print("count in else ", i, "is ", count)
        # if i == count:
        #     count = count + 1
    print("count of ", i, "is ", count)

from collections import Counter

Sample = [1, 2, 4, 5, 5, 5, 4, 4, 2, 3, 3, 2, 6, 2, 7, 7]
count = Sample.count(4)
print("count is ", count)

print(Counter(Sample))
# Counter({2: 4, 4: 3, 5: 3, 3: 2, 7: 2, 1: 1, 6: 1})


z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
print(Counter(z))
# Counter({'blue': 3, 'red': 2, 'yellow': 1})

zz = 'zunjarrdorugadde@gmail.com'
print(Counter(zz))
# -------------------------------------------------
# -------------------------------------------------
age = [5, 7, 18, 19, 21, 31]

# def voting(x):
#     if x > 18:
#         return True
#     else:
#         return False
#
#
# adult = filter(voting, age)
#
# for x in adult:
#     print(x)

# OR
# age = [5, 7, 18, 19, 21, 31]
# adults = filter(lambda a: a > 18, age)
#
# for x in adults:
#     print(x)
# -------------------------------------------------
# val = [6, 7, 18, 19, 22, 31]
#
# num = list(filter(lambda b: b % 2 == 0, val))
#
# for i in num:
#     print(i)
# -------------------------------------------------
a = {6, 7, 18, 19, 22, 31}
d = {}
for i in a:
    if i in d:
        d[i] = d[i] + 1
        print(d[i])
    else:
        d[i] = 1
        print('else part is ', d[i])
# -------------------------------------------------
# Sony Singh Auther

# City Bank

# s="welcome to python worl"
# strlen = len(s)
# print(strlen)
# d = {}
# num = 0
# for i in s:
#     if i

# d={1:'a',2:'b',1:'c'}


#
# print(s[::-1])
# vowel = ['a', 'e', 'i', 'o', 'u']
# d = {}

# for i in s:
#     if i in vowel:
#         d[i] = d.get(i,0) +1

# print(d)


# def square(**x):

#     for i in x:
#         yield (i*i)

#     return i*i

# x=[1,2,3,4]
# print(square(**x))

x = [1, 2, 3, 4]
d = {}
for i in x:
    d[i] = i * i
print(d)

# employee table column name is firstname, lastname, salary, empid is there

# Give me first name, last name of top 5 memeber having highest salary

# Select firstname, lastname from employee
# Where max(salary) limit 5
# -------------------------------------------------

# Demo_file

# s1={1,2,3,[1,2,3]}
# print(s1)

# s2={1,2,3,(1,2,3,1, 2)}
# print(s2)

# s3={1,2,3,{1,2,3}}
# print(s3)


# class A:
#
#     def m1(self):
#         return 7
#
#
#
# class B(A):


#
# str1 = 'ms14yst76echno92logi12es'
# output = [12, 14, 76, 92]
#
# emplst = []
# for i in str1:
#     if i.isdigit():
#         emplst = emplst.append(i)
#         print(emplst)
#         # output = sorted(emplst)
#         # print(output)
#
# behave -v test.feature --browser = chrome
#
#
# a,b=[10,100],[10,100]
# print(a==b)
# print(a is b)
#
#
# Vaibhavkumar Baviskar5:45 PM
# T
# T
# a,b=10,10
# print(a==b)
# print(a is b)
#
#
# Vaibhavkumar Baviskar5:47 PM
# s1={1,2,3,[1,2,3]}
# print(s1)
# s2={1,2,3,(1,2,3)}
# print(s2)
# s3={1,2,3,{1,2,3}}
# print(s3)

# -------------------------------------Synechrone-----------------------------------

# def read_data():
#     with open('C:/download/file.txt', 'r') as f:
#         data = f.read()
#         for i in data:
#             if i == @:
#                 i.remove
#
#         return data
#
#
# with open('C:/download/file.txt', 'w') as f:
#     data1 = f.write()
#
# 100
# 5 % Compund
# 200
#
# (100 * 0.05 * Year) / 100 = 200
#
# 100 + 5 = 105
# 105 + (10.5 / 2) =
#
# 200 / 0.05
#
# 20000 / 5 = 4000
#
# Chrome
# url
# 2
# text
# box
# Ok
# button
# new
# window
# verify
# link
# on
# window
#
# serv_obj = Service('C:/download/chromedriver.exe')
# driver = webdriver.Chrome(service=serv_obj)
#
# driver.get('www.facebook.com/')
# driver.implicitly_wait(10)
#
# driver.find_element(By.XPATH, "//input[text()='username']")
# driver.find_element(By.XPATH, "//input[text()='password']")
# driver.find_element(By.ID, "//button[id='submit']")
#
# handle = driver.current_window_handle
# driver.switch_to.window(handle)
#
# driver.find_element(By.LINKTEXT, "//a[text()='post']")
#
# screenshot
#
# driver.save_screenshot('C:/project/verify_link.png')
#
# Scenario: Check
# payment
# functionality
#
# feature: Verify
# payment
# done
# successfully
# GIVEN:
# WHEN:
# THEN:
# ------------------------------------------------------------------------

# demo_10

# Josh Software Prasad
import requests

count = 0
while True:
    if count % 3 == 0:
        print(count, end=" ")
    if (count > 15):
        break
    count += 1

# 1. 0,1,2... 15
# 2. Infinite Loop
# 3. 0,3,6,9,12,15  True
# 4. 0,3,6,9,12
# -----------------------------------------

# https://www.cleartrip.com/
# -----------------------------------------

# status codes: 201,402,404,501
# -----------------------------------------

# Input: Selenium --> Output: Sel, eni, um_

# str2 = input('Enter string: ')
# lenth = len(str2)
# emp_list = []
# new_char = []
# for i in range(2, lenth+1):
#     if lenth % i == 1:
#         for i in str2:
#             new_char.append(str2[-1:])
#
# print(new_char)


url = 'https://reqres.in/api/users?page=2'

response = requests.get(url)
dict_resp = response.json()
# print(dict_resp)
print(f'\n', dict_resp['data'])
# print(dict_resp['data'][4]['email'])
# print(dict_resp['id'])
new_id = input('Enter id: ')

for i in dict_resp['data']:
    # if i['id'] == new_id:
    #     print(i['email'])
    #     break

    # if i['email']
    # print(i['email'])
    # print(len(dict_resp['data']))
    for j in range(len(dict_resp['data'])):
        if j['id'] == new_id:
            # print(i['email'])
            print(dict_resp['data'][j]['email'])
            break
        # if dict_resp['data'][i]['id'] == num:
        #     print(dict_resp['data'][i]['email'])
# -------------------------------------------------------------
# demo15


from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from sdict import sortdict
import json

dct = {'sizes': [32, 28, 42], 'dog': 'schnauser', 'cat': 'siamese', 'bird': 'falcon'}
dctx = sortdict(dct)
print(json.dumps(dctx))

dict1 = {[1, 2]: 'a', (5, 7): 'b', {7, 9}: 'z', 3: 'g', 7: 'as'}  # TypeError: unhashable type: 'list'

# dict1 = {1: 'a', 2: 'b', 4: 'z', 3: 'g', 7: 'as'}
print(dict1)


# for k, v in sorted(dict1.items()):
#     print(dict1[k], ':', dict1[v])
#
# for k in sorted(dict1):
#     print(dict1[k])

# serv_obj = Service('C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver.exe')
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(10)
#
# driver.get(
#     'https://www.goibibo.com/flights/?utm_source=google&utm_medium=cpc&utm_campaign=DF-Brand-EM&utm_adgroup=Only+Goibibo&utm_term=%21SEM%21DF%21G%21Brand%21RSA%21108599293%216504095653%21602838584772%21e%21goibibo%21c%21&gclid=Cj0KCQjw2cWgBhDYARIsALggUhrMf73JuW5VU8xso6ioZRUfrY1VPTf8_49OxirmxZTKcyUNoFM4_0caAg7OEALw_wcB')
#
# one_way = driver.find_element(By.XPATH, '//ul[@class="sc-gsNilK hRWUSL"]/li/span')
# selected = one_way.is_selected()
# if selected == True:
#     print("By default one way is not selected")
#
# try:
#     flight = driver.find_element(By.XPATH, '//a[@class="nav-link active"]')
# except:
#     print('Not selected')
# -------------------------------------------------------------
# demo7

# Innova Solutions

def num(n):
    for i in range(n):
        yield i

    return i


num_seq = num(11)
print(next(num_seq))
print(next(num_seq))
print(next(num_seq))

list2 = [1, 2, 3, 4, 5, 7, 8, 9, 10]

for j in list2:
    if j not in num_seq:
        print(j)

# import requests

# response = requests.get('www.yahoo.com/user?page=2', auth=(username='xyz', password='dag@324'))
# print(response.status_code)

# requests.delete('www.yahoo.com/user=2')

# //table[@class='user']/tbody/tr[]/td[][text()='Name']

# Select customer_name from cust_table
# limit 10


# def test(a, b):
#     return a / b
#
# def outer(func):
#     def inner(a, b):
#         if a < b:
#             a, b = b, a
#             return func(a, b)
#
#     return inner()
#
# test = outer(test(2, 4))
# print(test)

str = '     ansb    dhcfhv     '

# str[-2:-1:]

var = str.strip()

var = var.split(' ')
print(var)
str2 = []
for i in var:
    str2.append(i)
    # print(str2)

print(" ".join(str2))

# www.google.com/getCustomer/1234567


# items['item'[0]['batters']['batter'][3]['type']]

# items['item'[1]['topping'][4]['type']]
