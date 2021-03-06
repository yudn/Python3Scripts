#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/2 11:56'

"""
1.17  从字典中提取子集 

问题:
  你想构造一个字典,它是另外一个字典的子集。

解决方案:
  最简单的方式是使用字典推导。
  
字典推倒式效率更高
"""

import time

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

t0 = time.time()
# Make a dictionary of all prices over 200    Best one
p1 = {key: value for key, value in prices.items() if value > 200}
t1 = time.time()

print(p1)

# 大多数情况下字典推导能做到的,通过创建一个元组序列然后把它传给dict()函数也能实现
# 但是，字典推导式p1比用dict()函数p3更快

t2 = time.time()
p3 = dict((key, value) for key, value in prices.items() if value > 200)
t3 = time.time()

print(p3)

print("p1 time: ", (t1-t0))
print("p3 time: ", (t3-t2))



# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
t4 = time.time()
p2 = {key: value for key, value in prices.items() if key in tech_names}
t5 = time.time()
print(p2)


# p2的另外一种实现方式   比p2的实现方式慢1.6倍
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
t6 = time.time()
p22 = {key: prices[key] for key in prices.keys() & tech_names}
t7 = time.time()
print(p22)

print("p2 time: ", (t5-t4))
print("p22 time: ", (t7-t6))

