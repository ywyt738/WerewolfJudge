#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
这是一个狼人杀首夜法官工具
版本:Ver0.5.1
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
if wizard_in == 1:
    wizard_saveself = wizard_save_self()
guard_in = role('守卫')
if wizard_in == 1 and guard_in == 1:
    guard_and_save = numput.raw_int('同守同救是否允许(0为不允许，1为允许)？')
# 生成玩家身份序列
player_role = ['村民'] * player_num
# 生成死亡玩家序列
today_dead = []

# 首夜
cls = os.system('cls')  # 天黑前清屏

# 守卫阶段
if guard_in == 1:
    guarded_player, guard_num = guard()

# 狼人阶段
killed_player, wwteam = werewolf(ww_number)
if killed_player == 0:
    pass
else:
    today_dead.append(killed_player)
# 将狼人加入玩家身份序列
for i in wwteam:
    player_role[int(i) - 1] = '狼人'

# 预言家阶段
if farseer_in == 1:
    farseer_num = farseer(player_role)

# 女巫阶段
if wizard_in == 1:
    save, poisoned_num, wizard_num = wizard(
        killed_player, wizard_saveself)
    # 解药使用情况
    if save == 1:
        # 守卫，女巫都参与游戏。判断同守同救。
        if guard_in == 1:
            # 判断是否允许同守同救，guard_and_save值为0是不允许，值为1是允许。
            if guard_and_save == 0:
                # 判断是否救的人是被杀杀的人
                if guard_num == killed_player:
                    # 被同守同救的人死亡
                    pass
                # 被杀的人不是被守护的人，使用了解药，正常复活
                else:
                    today_dead.pop()
            # 允许同守同救的情况下，同守同救，死者复活
            else:
                today_dead.pop()
        # 不存在守卫的情况，解药使用后，原来死亡的人复活
        else:
            today_dead.pop()
    if poisoned_num != 0:
        today_dead.append(poisoned_num)

# 没有女巫，有守卫参与的游戏情况
if guard_in == 1 and wizard_in == 0:
    if guarded_player == killed_player:
        killed_player = 0
        today_dead.pop()

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
    print('今晚死亡的玩家是：%s' % str(today_dead)[1:len(str(today_dead)) - 1])

# 将身份加入玩家身份序列
if farseer_in == 1:
    player_role[farseer_num - 1] = '预言家'
if guard_in == 1:
    player_role[guard_num - 1] = '守卫'
if wizard_in == 1:
    player_role[wizard_num - 1] = '女巫'

# 开启上帝视角
input('<回车开启上帝视角>')
i = 1
while i <= player_num:
    print('%d号玩家：%s。' % (i, player_role[i - 1]))
    i += 1

input()
