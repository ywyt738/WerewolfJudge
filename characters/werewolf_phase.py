#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
狼人的行动模块
input:玩家身份列表
output:击杀玩家号码，狼人队列
'''

__author__ = 'HuangXiaojun'

import os
import winsound
import time
import numput

wav_start = r".\audio\werewolf_st.wav"
wav_finish = r".\audio\werewolf_fi.wav"


def werewolf_phase(wws):
    cls = os.system('cls')
    winsound.PlaySound(wav_start, winsound.SND_NODEFAULT)  # 唤醒狼人
    while True:
        tem_ww_team = input('狼人请输入你们的号码(用空格分割)：')
        # 将输入狼队的空格去掉
        _ww_team = tem_ww_team.split(' ')
        if len(_ww_team) == wws:
            break
        else:
            print('本局有 %d 位狼人,输入人数不正确，请重新输入。' % wws)
    # 狼人杀人时间
    _killed_num = numput.raw_int('请输入你们想要杀的玩家号码（0为空刀）：')
    input('<回车继续>')
    print('狼人闭眼。')
    winsound.PlaySound(wav_finish, winsound.SND_NODEFAULT)  # 狼人闭眼
    time.sleep(3)
    return _killed_num, _ww_team
