#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
狼人的行动模块
input:玩家身份列表
output:击杀玩家号码
'''

__author__ = 'HuangXiaojun'

import os
import winsound
import time
import numput


def werewolf_phase():
    cls = os.system('cls')
    winsound.Beep(1000, 1000)  # 唤醒狼人
    tem_ww_team = input('狼人请输入你们的号码(用空格分割)：')
    # 将输入狼队的空格去掉
    _ww_team = []
    for a in list(tem_ww_team):
        if a == ' ':
            continue
        else:
            _ww_team.append(a)
    # 狼人杀人时间
    _killed_num = numput.raw_int('请输入你们想要杀的玩家号码（0为空刀）：')
    input('<回车继续>')
    print('狼人闭眼。')
    time.sleep(3)
    return _killed_num, _ww_team
