#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-25 10:01'

"""
汉诺塔：汉诺塔（又称河内塔）问题是源于印度一个古老传说的益智玩具。
大梵天创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序摞着64片黄金圆盘。
大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。
并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘。

这类问题不使用递归不好解决

思路：
n个盘子时：
1.把n-1个圆盘从A经过C移动到B
2.把第n个圆盘从A移动到C
3.把n-1个圆盘从B经过A移动到C
"""

def hanoi(n:int, A:str, B:str, C:str):
    """
    汉诺塔解法
    :param n: 问题规模
    :param A: 起始盘子
    :param B: 路过盘子
    :param C: 目标盘子
    :return: 操作路径
    """
    if n > 0:
        hanoi(n-1, A, C, B)        # 1.把n-1个圆盘从A经过C移动到B
        print("%s->%s" % (A, C))   # 2.把第n个圆盘从A移动到C
        hanoi(n-1, B, A, C)        # 3.把n-1个圆盘从B经过A移动到C

hanoi(2, "A", "B", "C")
print("*"*40)
hanoi(3, "A", "B", "C")