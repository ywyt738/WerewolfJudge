#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
预言家的行动模块
input:玩家身份列表
output:预言家号码
'''

__author__ = 'HuangXiaojun'

import os
import winsound
import time
import numput

wav_start = r".\audio\farseer_st.wav"
wav_finish = r".\audio\farseer_fi.wav"


def farseer_phase(role_list):
    '''预言家阶段'''
    cls = os.system('cls')
    winsound.PlaySound(wav_start, winsound.SND_NODEFAULT)  # 唤醒预言家
    _farseer = numput.raw_int('预言家，请输入你的号码：')
    _check_num = numput.raw_int('请输入你要查看的人的号码：')
    print('你查看的人是：%d号。他是：%s。' % (_check_num, role_list[_check_num - 1]))
    input('<回车继续>')
    print('预言家闭眼。')
    winsound.PlaySound(wav_finish, winsound.SND_NODEFAULT)  # 预言家闭眼
    time.sleep(3)
    return _farseer
