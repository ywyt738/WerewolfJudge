#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
定义纯数字输入方法，判断是否输入为全数字
input:提示输入时候的文字提示
'''

__author__ = 'HuangXiaojun'


def raw_int(tips):
    while True:
        num = input(tips)
        if num.isdigit():
            break
        else:
            print('你输入的不是数字!请重新输入。\n')
    return int(num)
