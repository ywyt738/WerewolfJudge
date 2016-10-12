#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
女巫模块
input:死亡玩家号码，自救开关
output:解药是否使用，毒死几号玩家，女巫号码
'''

__author__ = 'HuangXiaojun'


import os
import winsound
import time
import numput

wav_start = r".\audio\wizard_st.wav"
wav_finish = r".\audio\wizard_fi.wav"

def wizard_phase(dead, save_self):
    '''女巫阶段，反馈解救情况，毒死玩家号码和女巫号码'''
    cls = os.system('cls')
    winsound.PlaySound(wav_start, winsound.SND_NODEFAULT)  # 唤醒女巫
    _wizard = numput.raw_int('女巫，请输入你的号码：')
    print('注意：女巫一晚不能同时使用两瓶药！')
    _use_save = 0
    _use_poison = 0
# 解药阶段
    # 女巫死亡情况下
    if dead == _wizard:
        # 允许自救
        if save_self == 1:
            print('今晚你死了。')
            _whether_use = input('你要使用解药吗(y/n)？')
        #不允许自救
        else:
            print('今晚你死了，不能自救。')
            _whether_use = 'n'
    # 非女巫死亡情况
    else:
        # 空刀情况
        if dead == 0:
            print('今晚没人死。')
            _whether_use = 'n'
        # 非女巫玩家死亡
        else:
            print('今晚%d号死了。' % dead)
            _whether_use = input('你要使用解药吗(y/n)？')
    # 如果解药使用了，输入情况为‘y’或者‘Y’时，赋_use_save值为1，表示解药已经使用
    if _whether_use == 'y' or _whether_use == 'Y':
        _use_save = 1
# 毒药阶段
    # 没有使用解药，才能使用毒药
    if _use_save == 0:
        # 毒药使用情况，0为不使用，非0为使用毒药。
        _use_poison = numput.raw_int('你有瓶毒药是否要用？（输入想要毒死的号码，0为不使用）：')
    input('<回车继续>')
    print('女巫闭眼。')
    winsound.PlaySound(wav_finish, winsound.SND_NODEFAULT)  # 女巫闭眼
    time.sleep(3)
    # 返回解药使用情况，毒药使用情况，女巫号码
    # _use_save值1为使用解药，0为没使用解药
    # _use_poison值为0不使用毒药，不为0使用毒药，且是毒杀号码。
    # _wizard值为女巫号码
    return (_use_save, _use_poison, _wizard)


def self_switch():
    wizard_saveself = input('女巫是否能自救(y/N)？')
    if wizard_saveself == '' or wizard_saveself == 'n' or wizard_saveself == 'N':
        wizard_saveself = 0
    else:
        wizard_saveself = 1
    return wizard_saveself
