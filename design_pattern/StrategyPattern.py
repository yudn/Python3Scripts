#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/25 13:34'

"""
大话设计模式Python实现-策略模式

02.策略模式(Strategy Pattern):
它定义了算法家族,分别封装起来,让他们之间可以相互替换,此模式让算法变化,不会影响到使用算法的客户.

模式特点：定义算法家族并且分别封装，它们之间可以相互替换而不影响客户端。

程序实例：商场收银软件，需要根据不同的销售策略方式进行收费

代码特点：不同于用例1，这里使用字典是为了避免关键字不在字典导致bug的陷阱。

https://www.cnblogs.com/wuyuegb2312/archive/2013/04/09/3008320.html

"""


