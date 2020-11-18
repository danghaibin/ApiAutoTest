#!/usr/bin/env python3.8.5
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 21:02
# @Author  : Danghaibin
# @FileName: demo111.py
# @Software: PyCharm
import string
list = ['a','b','c']

for i in range(len(list)):
    a  = f"{i+1}.{list[i]}"
    print(a,end='')
import keyword
print(len(keyword.kwlist))

print(keyword)