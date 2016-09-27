#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
这是一个狼人杀首夜法官工具
版本:v0.2
支持角色：女巫，先知
v0.2
- 新增女巫自救开关
'''
import os
import winsound
import time

#定义纯数字输入方法
def raw_int(tips):
    '''定义纯数字输入方法，判断是否输入为全数字'''
    while True:
        num = input(tips)
        if num.isdigit():
            break
        else:
            print('你输入的不是数字!请重新输入。\n')
    return int(num)

#使用角色询问方法
def role(role):
    '''role是否有？'''
    #role有的话就返回1，没有返回0
    _role_in = input('是否有%s(Y/n)?' % role)
    if _role_in == '' or _role_in == 'y' or _role_in =='Y':
        return 1
    else:
        return 0

def werewolf_phase(role_list):
    '''狼人阶段，反馈击杀玩家号码'''
    cls = os.system('cls')
    winsound.Beep(1000,1000)#唤醒狼人
    tem_ww_team = input('狼人请输入你们的号码(用空格分割)：')
    #将输入狼队的空格去掉
    _ww_team = []
    for a in list(tem_ww_team):
        if a == ' ':
            continue
        else:
            _ww_team.append(a)
    #狼人杀人时间
    _killed_num = raw_int('请输入你们想要杀的玩家号码（0为空刀）：')
    #将狼人加入玩家身份序列
    for i in _ww_team:
        role_list[int(i)-1] = '狼人'
    input('<回车继续>')
    print('狼人闭眼。')
    time.sleep(3)
    return _killed_num

def farseer_phase(role_list):
    '''先知阶段'''
    cls = os.system('cls')
    winsound.Beep(1000,1000)#唤醒先知
    _farseer = raw_int('先知，请输入你的号码：')
    _check_num = raw_int('请输入你要查看的人的号码：')
    print('你查看的人是：%d号。他是：%s。' % (_check_num, role_list[_check_num-1]) )
    #将先知加入玩家身份序列
    role_list[_farseer-1] = '先知'
    input('<回车继续>')
    print('先知闭眼。')
    time.sleep(3)
    return

def wizard_phase(dead,l,save_self):
    '''女巫阶段，反馈解救情况和毒死玩家号码'''
    cls = os.system('cls')
    winsound.Beep(1000,1000)#唤醒女巫
    _wizard = raw_int('女巫，请输入你的号码：')
    print('注意：女巫一晚不能同时使用两瓶药！')
    _use_save = 0
    _use_poison = 0
    #解药阶段
    if dead == _wizard:
        if save_self == 1:
            print('今晚你死了。')
            _whether_use = input('你要使用解药吗？(y/n)')
        else:
            print('今晚你死了，不能自救。')
            _whether_use = 'n'
    else:
        print('今晚%d号死了。' % dead)
        _whether_use = input('你要使用解药吗？(y/n)')
    if _whether_use == 'y' or _whether_use == 'Y':
        _use_save = 1
    #毒药阶段
    if _use_save == 0:
        _use_poison = raw_int('你有瓶毒药是否要用？（输入想要毒死的号码，0为不使用）')
    #将女巫加入玩家身份序列
    l[_wizard-1] = '女巫'
    input('<回车继续>')
    print('女巫闭眼。')
    time.sleep(3)
    return (_use_save,_use_poison)

#====================game start====================
#游戏启动清屏
cls = os.system('cls')
#输入游戏人数(最大12人，最少5人)
while True:
    player_num = raw_int('请输入游戏人数，最多12人：')
    if player_num > 12:
        print('输入人数必须小于12。')
    elif player_num >=5:
        break
    else:
        print('人这么少玩个P啊。')
 #输入狼人人数（狼人数必须小于玩家人数）
while True:
    ww_number = raw_int('请输入狼人人数：')
    if ww_number > player_num:
        print('狼人数必须小于玩家人数。现有玩家%d名。' % player_num)
    elif ww_number >=1:
        break
    else:
        print('没狼玩个P啊。')

#游戏配置设置。（最大支持：女巫、预言家）
wizard_in = role('女巫')
#女巫是否能自救设置
wizard_saveself = input('女巫是否能自救(y/N)？：')
if wizard_saveself == '' or wizard_saveself == 'n' or wizard_saveself == 'N':
    wizard_saveself = 0
else:
    wizard_saveself = 1
farseer_in = role('先知')

player_role = ['好人']*player_num#生成玩家身份序列
player_stat = ['存活']*player_num#生存玩家存活序列
today_dead = []#生成死亡玩家序列

#首夜
cls = os.system('cls')#天黑前清屏
#狼人阶段
killed_player = werewolf_phase(player_role)
if killed_player == 0:
    pass
else:
    player_stat[killed_player-1] = '死亡'
    today_dead.append(killed_player)

#先知阶段
#print(farseer_in)
if farseer_in == 1:
    farseer_phase(player_role)

#女巫阶段
if wizard_in ==1:
    save,poisoned_num = wizard_phase(killed_player, player_role,wizard_saveself)
    if save == 1:
        player_stat[killed_player-1] = '存活'
        today_dead.pop()
    if poisoned_num != 0:
        player_stat[poisoned_num-1] = '死亡'
        today_dead.append(poisoned_num)

#天亮了
cls = os.system('cls')
winsound.Beep(1000,1000)#天亮
#死亡号码排序
today_dead.sort()
print('请参与警长选举的玩家一起举手。')
input('<回车发布今晚死讯>')
if today_dead == []:
    print('今晚平安夜。')
else:
    print('今晚死亡的玩家是%s' % today_dead)
input('<回车开启上帝视角>')
i = 1
while i <= player_num:
    print('%d号玩家：%s。' %(i,player_role[i-1]))
    i += 1
