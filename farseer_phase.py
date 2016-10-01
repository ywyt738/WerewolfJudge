#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
先知的行动模块
input:玩家身份列表
output:None
'''

__author__ = 'HuangXiaojun'

import os
import winsound
import time
import numput


def farseer_phase(role_list):
    '''先知阶段'''
    cls = os.system('cls')
    winsound.Beep(1000, 1000)  # 唤醒先知
    _farseer = numput.raw_int('先知，请输入你的号码：')
    _check_num = numput.raw_int('请输入你要查看的人的号码：')
    print('你查看的人是：%d号。他是：%s。' % (_check_num, role_list[_check_num - 1]))
    input('<回车继续>')
    print('先知闭眼。')
    time.sleep(3)
    return _farseer
