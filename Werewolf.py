#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
这是一个狼人杀首夜法官工具
版本:Ver0.4.0
支持角色：女巫，预言家，守卫
'''
__author__ = 'HuangXiaojun'

import os
import winsound

import numput
from characters.werewolf_phase import werewolf_phase as werewolf
from characters.farseer_phase import farseer_phase as farseer
from characters.wizard_phase import wizard_phase as wizard
from characters.wizard_phase import self_switch as wizard_save_self
from characters.guard_phase import guard_phase as guard


def role(role):
    '''role是否有？'''
    # role有的话就返回1，没有返回0
    _role_in = input('是否有%s(Y/n)？' % role)
    if _role_in == '' or _role_in == 'y' or _role_in == 'Y':
        return 1
    else:
        return 0

#====================game start====================
# 游戏启动清屏
cls = os.system('cls')
# 输入游戏人数(最大12人，最少5人)
while True:
    player_num = numput.raw_int('请输入游戏人数，最多12人：')
    if player_num > 12:
        print('输入人数必须小于12。')
    elif player_num >= 5:
        break
    else:
        print('人这么少玩个P啊。')
 # 输入狼人人数（狼人数必须小于玩家人数）
while True:
    ww_number = numput.raw_int('请输入狼人人数：')
    if ww_number > player_num:
        print('狼人数必须小于玩家人数。现有玩家%d名。' % player_num)
    elif ww_number >= 1:
        break
    else:
        print('没狼玩个P啊。')

# 游戏配置设置。（最大支持：女巫、预言家、守卫）
farseer_in = role('预言家')
wizard_in = role('女巫')
# 女巫是否能自救设置
wizard_saveself = wizard_save_self()
guard_in = role('守卫')

player_role = ['好人'] * player_num  # 生成玩家身份序列
player_stat = ['存活'] * player_num  # 生存玩家存活序列
today_dead = []  # 生成死亡玩家序列

# 首夜
cls = os.system('cls')  # 天黑前清屏

# 狼人阶段
killed_player, wwteam = werewolf(ww_number)
if killed_player == 0:
    pass
else:
    player_stat[killed_player - 1] = '死亡'
    today_dead.append(killed_player)
# 将狼人加入玩家身份序列
for i in wwteam:
    player_role[int(i) - 1] = '狼人'

# 预言家阶段
if farseer_in == 1:
    farseer_num = farseer(player_role)

# 守卫阶段
if guard_in == 1:
    guarded_player, guard_num = guard()
    if guarded_player == killed_player:
        player_stat[killed_player - 1] = '存活'
        killed_player = 0
        today_dead.pop()

# 女巫阶段
if wizard_in == 1:
    save, poisoned_num, wizard_num = wizard(
        killed_player, wizard_saveself)
    if save == 1:
        player_stat[killed_player - 1] = '存活'
        today_dead.pop()
    if poisoned_num != 0:
        player_stat[poisoned_num - 1] = '死亡'
        today_dead.append(poisoned_num)

# 天亮了
cls = os.system('cls')
wav_dawn = r".\audio\dawn.wav"
winsound.PlaySound(wav_dawn, winsound.SND_NODEFAULT)  # 天亮
# 死亡号码排序
today_dead.sort()
print('请参与警长选举的玩家一起举手。')
# 宣布死讯
input('<回车发布今晚死讯>')
if today_dead == []:
    print('今晚平安夜。')
else:
    print('今晚死亡的玩家是：%s' % today_dead)

# 将身份加入玩家身份序列
player_role[farseer_num - 1] = '预言家'
player_role[guard_num - 1] = '守卫'
player_role[wizard_num - 1] = '女巫'

# 开启上帝视角
input('<回车开启上帝视角>')
i = 1
while i <= player_num:
    print('%d号玩家：%s。' % (i, player_role[i - 1]))
    i += 1

input()
