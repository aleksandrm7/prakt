# 1
def fact(x):
  if (x <= 1):
      return 1
  else:
      return x * fact(x-1)

# 2

def filter_even(li):
  result = list(filter(lambda x: x % 2 == 0, li))
  return result

# 3

def square(li):
  return list(map(lambda x: x*x, li))

# 4

def bin_search(li, element):
    l = 0
    r = len(li) - 1
    while l <= r:
        m = (l+r) // 2
        if (li[m] == element):
            return m
        elif li[m] < element:
            l = m + 1
        else:
            r = m - 1
    return -1

# 5

def is_palindrome(string):
    string = string.lower().strip()
    for c in '.,?!\'():; ':
        string = string.replace(c, '')
    is_pln = True
    l = len(string)
    for i in range(l // 2):
        if string[i] != string[l-1-i]:
            is_pln = False
            break
    return is_pln

# 6

def calculate(path2file):
    try:
        with open(path2file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print('File', path2file, 'not found')
        return
    results = []
    for l in lines:
        sign, op1, op2 = l.strip().split('    ')
        op1 = int(op1)
        op2 = int(op2)
        if sign == '+':
            res = op1 + op2
        elif sign == '-':
            res = op1 - op2
        elif sign == '*':
            res = op1 * op2
        elif sign == '//':
            res = op1 // op2
        elif sign == '%':
            res = op1 % op2
        elif sign == '**':
            res = op1 ** op2
        results.append(str(res))
    return ",".join(results)

# 7

def substring_slice(path2file_1,path2file_2):
    try:
        with open(path2file_1, 'r') as f1:
            lines1 = f1.readlines()
        with open(path2file_2, 'r') as f2:
            lines2 = f2.readlines()
    except FileNotFoundError:
        print('File not found')
        return
    result = ''
    for i in range(len(lines1)):
        a, b = lines2[i].split()
        result += lines1[i][int(a):int(b) + 1] + ' '
    result = result[:-1]
    return result

# 8

import json

f = open('periodic_table.json', encoding='utf-8')
periodic_table = json.load(f)

def decode_ch(sting_of_elements):
    result = ''
    while sting_of_elements != '':
        elem = sting_of_elements[0]
        sting_of_elements = sting_of_elements[1:]
        while (len(sting_of_elements) > 0) and (not sting_of_elements[0].isupper()):
            elem += sting_of_elements[0]
            sting_of_elements = sting_of_elements[1:]
        result += periodic_table[elem]
    return result

# 9

class Student:
    def __init__(self, name, surname, grades=[3, 4, 5]):
        self.name = name
        self.surname = surname
        self.fullname = name + ' ' + surname
        self.grades = grades

    def greeting(self):
        print('Hello, I am Student ' + self.fullname)

    def mean_grade(self):
        return sum(self.grades) / len(self.grades)

    def is_otlichnik(self):
        if self.mean_grade() >= 4.5:
            return 'YES'
        else:
            return 'NO'

    def __add__(self, other):
        return '{0} is friends with {1}'.format(self.name, other.name)

    def __str__(self):
        return self.fullname

# 10

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return self.msg
