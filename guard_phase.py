#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
守卫的行动模块
input:玩家身份序列
output:守护玩家号码
'''

__author__ = 'HuangXiaojun'

import os
import winsound
import time
import numput


def guard_phase():
    '''守卫阶段，反馈守护玩家号码'''
    cls = os.system('cls')
    winsound.Beep(1000, 1000)  # 唤醒守卫
    _guard = numput.raw_int('守卫，请输入你的号码：')
    _guarded = numput.raw_int('请输入你要守卫的玩家号码：')
    input('<回车继续>')
    print('守卫闭眼。')
    time.sleep(3)
    return _guarded, _guard
