# -*- coding: utf-8 -*-
'''
这是一个狼人杀首夜法官工具GUI版本
版本:Ver0.6.3
支持角色：女巫，预言家，守卫
'''


from tkinter import *
import tkinter.messagebox as messagebox
import winsound
import os
from datetime import datetime


__author__ = 'HuangXiaojun'


# 图形界面
class main(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        # 游戏准备阶段
        self.ready()
        # 角色阶段置为未行动
        self.Werewolf_fi = False
        self.Guard_fi = False
        self.Farseer_fi = False
        self.Wizard_fi = False

    def phase(self):
        '''流程控制函数，每个阶段结束按钮行为函数都会call这个函数，来进行下个阶段的发起'''
        # 流程控制角色阶段执行变量改为True，表示上个阶段完成
        if self.Werewolf_fi == False:
            self.ww()
        elif self.Guard_in == 1 and self.Guard_fi == False:
            self.grd()
        elif self.Farseer_in == 1 and self.Farseer_fi == False:
            self.fse()
        elif self.Wizard_in == 1 and self.Wizard_fi == False:
            self.wzd()
        else:
            self.dawn()

    # 游戏配置阶段
    # 全程变量：玩家人数self.Player_num，狼人人数self.Werewolf_num，身份序列self.Player_role，死亡序列self.Today_dead
    # 预言家是否有self.Farseer_in，女巫是否有self.Wizard_in，女巫是否能自救self.Wizard_saveself，守卫是否有self.Guard_in
    def ready(self):
        # 定义游戏人数，狼人人数，预言家是否参与，女巫是否参与，女巫是否能自救，守卫是否参与变量
        self.Player_num = 0
        self.Werewolf_num = 0
        self.Farseer_in = 0
        self.Wizard_in = 0
        self.Wizard_saveself = 0
        self.Guard_in = 0

        # 开始按钮行为
        def start():
            # 游戏人数取值
            self.Player_num = player_num.get()
            # 狼人人数取值
            self.Werewolf_num = werewolf_num.get()
            # 预言家是否参与取值
            self.Farseer_in = farseer_in.get()
            # 女巫是否参与取值
            self.Wizard_in = wizard_in.get()
            # 女巫是否能够自救取值
            self.Wizard_saveself = wizard_saveself.get()
            # 守卫是否参与取值
            self.Guard_in = guard_in.get()
            # 定义角色变量转换dict
            join = {1: '有', 0: '无'}
            can = {1: '能', 0: '不能'}
            # 弹出游戏配置消息窗口
            messagebox.showinfo('游戏配置', '''
            玩家一共%d人，狼人%d人。
            预言家：%s
            女巫：%s。女巫%s自救。
            守卫：%s
            ''' % (self.Player_num, self.Werewolf_num, join[self.Farseer_in], join[self.Wizard_in], can[self.Wizard_saveself], join[self.Guard_in]))
            # 生成玩家身份列表
            self.Player_role = ['村民'] * self.Player_num
            # 生成死亡玩家序列
            self.Today_dead = []
            # 记录游戏配置日志到log.txt
            with open(r".\log.txt", 'a') as log_file:
                now = datetime.now()
                log_file.write(now.strftime('%b %d %H:%M\n') + '游戏配置：一共%d人，狼人%d人。预言家：%s。女巫：%s。守卫：%s。\n' % (
                    self.Player_num, self.Werewolf_num, join[self.Farseer_in], join[self.Wizard_in], join[self.Guard_in]))
            # 界面切换
            ready1.destroy()
            ready2.destroy()
            ready3.destroy()
            # 阶段结束，call流程函数
            self.phase()

        # 预言家是否使用取值变量
        farseer_in = IntVar()
        # 女巫是否使用取值变量
        wizard_in = IntVar()
        # 女巫是否能够自救取值变量
        wizard_saveself = IntVar()
        # 守卫是否使用取值变量
        guard_in = IntVar()
        # 游戏人数取值变量
        player_num = IntVar()
        # 狼人人数取值变量
        werewolf_num = IntVar()

        # >>>>>>>>>>>>>>>>>>>>>>>>>>人数选择ready1 frame
        ready1 = Frame()
        # 游戏人数设置label
        Label(ready1, text='请选择游戏人数：').pack()
        # 游戏人数选择拉条
        Scale(ready1, from_=5, to=12, resolution=1,
              orient='horizontal', variable=player_num,).pack()
        # 狼人人数设置label
        Label(ready1, text='请选择狼人数量：').pack()
        # 狼人人数选择拉条
        Scale(ready1, from_=1, to=11, resolution=1,
              orient='horizontal', variable=werewolf_num).pack()
        # 放置ready1 frame
        ready1.pack()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>角色选择ready2 frame
        ready2 = Frame()
        # 预言家是否参与选择框
        Checkbutton(ready2, text='预言家',
                    variable=farseer_in).grid(row=1, column=0)
        # 女巫是否参与选择框
        Checkbutton(ready2, text='女巫',
                    variable=wizard_in).grid(row=2, column=0)
        # 女巫自救选择框
        Radiobutton(ready2, text='不能自救', variable=wizard_saveself,
                    value=0, state=DISABLED).grid(row=2, column=1)
        Radiobutton(ready2, text='能自救', variable=wizard_saveself,
                    value=1, state=DISABLED).grid(row=2, column=2)
        # 守卫是否参与选择框
        Checkbutton(ready2, text='守卫',
                    variable=guard_in).grid(row=1, column=1)
        # 放置ready2 frame
        ready2.pack()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>游戏开始按钮ready3 frame
        ready3 = Frame()
        # 游戏开始按钮
        Button(ready3, text='开始游戏', command=start).pack()
        # 放置ready3 frame
        ready3.pack()

    # 狼人阶段
    # 全程变量：狼人队列self.Ww_team，被杀玩家号self.Killed_player，狼人阶段完成变量self.Werewolf_fi
    def ww(self):
        # 定义狼队，被杀玩家号码变量
        self.Ww_team = []
        self.Killed_player = 0
        # 狼人行动按钮行为

        def ww_go():
            # 通过狼人号码取值，生成狼队
            for i in range(self.Player_num):
                # 按钮没被选择取值为0，选中取值为1。
                a = adict['a' + str(i)].get()
                # 取值为1的加入狼队变量
                if a != 0:
                    self.Ww_team.append(a)
            # 击杀目标取值
            self.Killed_player = killed_num.get()
            # 将狼人号码记入身份序列，供预言家查看用。
            for i in self.Ww_team:
                self.Player_role[int(i) - 1] = '狼人'
            # 狼人行动信息弹窗
            messagebox.showinfo('狼人阶段信息', '''
            狼队：%s。
            今晚你们要击杀的是%s号。''' % (str(self.Ww_team)[1:-1], self.Killed_player))
            # 记入狼队以及狼队行动进日志log.txt
            with open(r".\log.txt", 'a') as log_file:
                log_file.write('狼队：%s。击杀%s\n' %
                               (str(self.Ww_team)[1:-1], self.Killed_player))
            # 狼人闭眼音效路径
            wav_finish = r".\audio\werewolf_fi.wav"
            # 播放狼人闭眼音效
            winsound.PlaySound(wav_finish, winsound.SND_NODEFAULT)
            # 界面切换
            ww1.destroy()
            ww2.destroy()
            ww3.destroy()
            # 阶段结束，call流程函数
            self.Werewolf_fi = True
            self.phase()

        # 狼人睁眼音效路径
        wav_start = r".\audio\werewolf_st.wav"
        # 播放狼人睁眼音效
        winsound.PlaySound(wav_start, winsound.SND_NODEFAULT)
        # 击杀目标取值变量
        killed_num = IntVar()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>狼队输入框架ww1 frame
        ww1 = Frame()
        # 狼人图片路径
        self.ww_pic = PhotoImage(file=r'.\pic\werewolf.gif')
        # 狼人图片label
        Label(ww1, image=self.ww_pic).pack()
        # 狼人号码输入label
        Label(ww1, text='狼人请选择你们的号码：').pack()
        # 狼人号码输入框生成
        adict = {}
        # 根据人数生成取值变量名
        for i in list(range(self.Player_num)):
            adict['a' + str(i)] = IntVar()
        # 生成狼人号码输入框，每个输入框对应一个取值变量
        for i in range(self.Player_num):
            Checkbutton(ww1, text=i + 1, onvalue=i + 1,
                        variable=adict['a' + str(i)]).pack(side="left")
        # 放置ww1 frame
        ww1.pack()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>狼队击杀目标选择框架ww2 frame
        ww2 = Frame()
        # 狼人击杀目标输入提示label
        Label(ww2, text='狼人请选择要击杀的目标(0为空刀)：').pack()
        # 生成击杀目标号码按钮
        for r in range(self.Player_num + 1):
            Radiobutton(ww2, text=r, value=r,
                        variable=killed_num).pack(side='left')
        # 放置ww2 frame
        ww2.pack()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>狼人行动确认按钮框架ww3 frame
        ww3 = Frame()
        # 狼人行动确认按钮
        Button(ww3, text='确定', command=ww_go).pack()
        # 放置ww3 frame
        ww3.pack()

    # 先知阶段
    # 全程变量：预言家号码self.Farseer_num
    def fse(self):
        # 预言家号码变量
        self.Farseer_num = 0
        # 预言家行动按钮行为

        def fse_go():
            # 获取预言家号码
            self.Farseer_num = farseer_num.get()
            # 预言家阶段信息弹窗
            messagebox.showinfo('验人结果', '你查看的人是：%d号。\n他是：%s。' % (
                check_num.get(), self.Player_role[check_num.get() - 1]))
            # 预言家行动记录日志log.txt
            with open(r".\log.txt", 'a') as log_file:
                log_file.write('%d是预言家，查看了%d号是%s。\n' % (
                    self.Farseer_num, check_num.get(), self.Player_role[check_num.get() - 1]))
            # 预言家闭眼音效
            wav_finish = r".\audio\farseer_fi.wav"
            # 播放预言家闭眼音效
            winsound.PlaySound(wav_finish, winsound.SND_NODEFAULT)
            # 界面切换
            fe1.destroy()
            fe2.destroy()
            fe3.destroy()
            # 阶段结束，call流程函数
            self.Farseer_fi = True
            self.phase()

        # 预言家睁眼音效路径
        wav_start = r".\audio\farseer_st.wav"
        # 播放预言家真眼音效
        winsound.PlaySound(wav_start, winsound.SND_NODEFAULT)
        # 预言家号码取值变量
        farseer_num = IntVar()
        # 验人号码取值变量
        check_num = IntVar()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>预言家号码输入框架fe1 frame
        fe1 = Frame()
        # 预言家图片路径
        self.fse_pic = PhotoImage(file=r'.\pic\farseer.gif')
        # 预言家图片label
        Label(fe1, image=self.fse_pic).pack()
        # 预言家输入提示label
        Label(fe1, text='预言家输入你的号码：').pack()
        # 预言家号码读取按钮
        for r in range(1, self.Player_num + 1):
            Radiobutton(fe1, text=r, value=r,
                        variable=farseer_num).pack(side='left')
        # 放置fe1框架
        fe1.pack()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>预言家验人输入框架fe2 frame
        fe2 = Frame()
        # 预言家验人输入提示label
        Label(fe2, text='请输入你要查看的号码：').pack()
        # 预言家验人输入按钮
        for r in range(1, self.Player_num + 1):
            Radiobutton(fe2, text=r, value=r,
                        variable=check_num).pack(side='left')
        # 放置fe2框架
        fe2.pack()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>预言家行动确认按钮框架fe3 frame
        fe3 = Frame()
        # 预言家行动按钮
        Button(fe3, text='确定', command=fse_go).pack()
        # 放置fe3框架
        fe3.pack()

    # 守卫阶段
    # 全程变量：守卫号码self.Guard_num，被保护人号码self.Protect_num
    def grd(self):
        # 守卫号码变量
        self.Guard_num = 0
        # 被守人号码变量
        self.Protect_num = 0
        # 守卫行动按钮行为

        def grd_go():
            # 获取守卫号码
            self.Guard_num = guard_num.get()
            # 被守人号码
            self.Protect_num = protect_num.get()
            # 守卫阶段信息弹窗
            messagebox.showinfo('守卫信息', '今晚你保护的人是：%d号。' % (protect_num.get()))
            # 守卫行动记录日志log.txt
            with open(r".\log.txt", 'a') as log_file:
                log_file.write('%d是守卫，守护了%d号。\n' % (
                    self.Guard_num, self.Protect_num))
            # 守卫闭眼音效
            wav_finish = r".\audio\guard_fi.wav"
            # 播放守卫闭眼音效
            winsound.PlaySound(wav_finish, winsound.SND_NODEFAULT)
            # 界面切换
            gd1.destroy()
            gd2.destroy()
            gd3.destroy()
            # 阶段结束，call流程函数
            self.Guard_fi = True
            self.phase()

        # 守卫睁眼音效路径
        wav_start = r".\audio\guard_st.wav"
        # 播放守卫真眼音效
        winsound.PlaySound(wav_start, winsound.SND_NODEFAULT)
        # 守卫取值变量
        guard_num = IntVar()
        # 被守护人号码
        protect_num = IntVar()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>守卫号码输入框架gd1 frame
        gd1 = Frame()
        # 守卫图片路径
        self.grd_pic = PhotoImage(file=r'.\pic\guard.gif')
        # 守卫图片label
        Label(gd1, image=self.grd_pic).pack()
        # 守卫输入提示label
        Label(gd1, text='守卫输入你的号码：').pack()
        # 守卫号码读取按钮
        for r in range(1, self.Player_num + 1):
            Radiobutton(gd1, text=r, value=r,
                        variable=guard_num).pack(side='left')
        # 放置gd1框架
        gd1.pack()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>预言家验人输入框架gd2 frame
        gd2 = Frame()
        # 守卫守人输入提示label
        Label(gd2, text='请输入你要保护的号码：').pack()
        # 守卫验人输入按钮
        for r in range(1, self.Player_num + 1):
            Radiobutton(gd2, text=r, value=r,
                        variable=protect_num).pack(side='left')
        # 放置gd2框架
        gd2.pack()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>守卫行动确认按钮框架gd3 frame
        gd3 = Frame()
        # 守卫行动按钮
        Button(gd3, text='确定', command=grd_go).pack()
        # 放置gd3框架
        gd3.pack()

    # 女巫阶段
    # 全程变量：女巫号码self.Wizard_num，用药情况self.Dug
    def wzd(self):
        # 女巫号码变量
        self.Wizard_num = 0
        # 用药变量定义
        self.Dug = -1
        # 女巫行动按钮行为

        def wzd_go():
            # 女巫号码取值
            self.Wizard_num = wizard_num.get()
            # 用药变量取值
            self.Dug = dug.get()
            # 女巫阶段信息弹窗
            # 女巫使用解药的情况
            if self.Dug == 0:
                # 女巫用解药弹窗信息
                messagebox.showinfo('女巫信息', '今天晚上%s号死了，你解救了他/她。' %
                                    self.Killed_player)
                # 女巫行动记录日志log.txt
                with open(r".\log.txt", 'a') as log_file:
                    log_file.write('%d是女巫。使用了解药。\n' %
                                   self.Wizard_num)
            # 女巫使用毒药的情况
            elif self.Dug != 99:
                # 女巫使用毒药弹窗信息
                messagebox.showinfo('女巫信息', '今天晚上%s号死了，你没有使用解药，并且你下毒杀死了%s号。' % (
                    self.Killed_player, self.Dug))
                # 女巫行动记录日志log.txt
                with open(r".\log.txt", 'a') as log_file:
                    log_file.write('%d是女巫。使用了毒药，毒死了%d号。\n' % (
                        self.Wizard_num, self.Dug))
            # 女巫不用药的情况
            elif self.Dug == 99:
                # 女巫不用药弹窗信息
                messagebox.showinfo(
                    '女巫信息', '今天晚上%s号死了，你没有使用解药和毒药。' % self.Killed_player)
                with open(r".\log.txt", 'a') as log_file:
                    log_file.write('%d是女巫。没有使用解药和毒药。\n' %
                                   self.Wizard_num)
            # 女巫闭眼音效路径
            wav_finish = r".\audio\wizard_fi.wav"
            # 播放女巫闭眼音效
            winsound.PlaySound(wav_finish, winsound.SND_NODEFAULT)
            # 界面切换
            wd1.destroy()
            wd2.destroy()
            wd3.destroy()
            # 阶段结束，call流程函数
            self.Wizard_fi = True
            self.phase()

        # 女巫睁眼音效路径
        wav_start = r".\audio\wizard_st.wav"
        # 播放女巫真眼音效
        winsound.PlaySound(wav_start, winsound.SND_NODEFAULT)
        # 女巫号码取值变量
        wizard_num = IntVar()
        # 解药、毒药使用情况取值变量
        dug = IntVar()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>女巫号码输入框架wd1 frame
        wd1 = Frame()
        # 女巫图片路径
        self.wd_pic = PhotoImage(file=r'.\pic\wizard.gif')
        # 女巫图片label
        Label(wd1, image=self.wd_pic).pack()
        # 女巫输入提示label
        Label(wd1, text='女巫输入你的号码：').pack()
        # 女巫号码读取按钮
        for r in range(1, self.Player_num + 1):
            Radiobutton(wd1, text=r, value=r,
                        variable=wizard_num).pack(side='left')
        # 放置wd1框架
        wd1.pack()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>女巫用药框架wd2 frame
        wd2 = Frame()
        # 今晚死亡信息，用药提示信息label。
        Label(wd2, text='今天晚上%s号死了。你是否要救？是否要用毒药？' %
              self.Killed_player).pack()
        # 解药使用按钮。使用解药dug变量取值0
        Radiobutton(wd2, text='救', value=0,
                    variable=dug).pack(side='left')
        # 毒药使用对象按钮，毒几号，dug取值几
        for r in range(1, self.Player_num + 1):
            Radiobutton(wd2, text=r, value=r,
                        variable=dug).pack(side='left')
        # 放置wd2框架
        wd2.pack()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>女巫不用药和行动确认按钮框架wd3 frame
        wd3 = Frame()
        # 不用药按钮，不用药dug取值99
        Radiobutton(wd3, text='解药、毒药都不用。',
                    value=99, variable=dug).pack()
        # 守女巫行动按钮
        Button(wd3, text='确定', command=wzd_go).pack()
        # 放置wd3框架
        wd3.pack()

    # 天亮阶段，结算
    def dawn(self):
        # 结算
        # self.Killed_player
        # self.Protect_num
        # self.Dug
        # self.Today_dead

        #狼人结算
        if self.Killed_player != 0:
            self.Today_dead.append(self.Killed_player)
        # 守卫结算
        if self.Guard_in == 1:
            if self.Killed_player == self.Protect_num:
                self.Today_dead.pop()
        # 女巫结算
        if self.Wizard_in == 1:
            tongshoutongjiu = False
            # 解药结算
            if self.Dug == 0:
                # 是否有守卫，判断同守同救
                if self.Guard_in == 1:
                    # 击杀的人被守护
                    if self.Protect_num == self.Killed_player:
                        # 允许则不向死亡序列中添加
                        if tongshoutongjiu == True:
                            pass
                        # 不允许则向死亡序列中添加被击杀玩家号码
                        else:
                            # 因为守卫结算已经移除了死亡号码，重新补回。
                            self.Today_dead.append(self.Killed_player)
                    # 击杀的人没有被守护
                    else:
                        self.Today_dead.pop()
                # 没有守卫
                else:
                    self.Today_dead.pop()
            # 没用解药也没用毒药
            elif self.Dug == 99:
                pass
            # 没用解药，使用了毒药
            else:
                self.Today_dead.append(self.Dug)
                
        # 排序死亡序列
        self.Today_dead.sort()
        # 天亮音效路径
        wav_dawn = r".\audio\dawn.wav"
        # 播放天亮音效
        winsound.PlaySound(wav_dawn, winsound.SND_NODEFAULT)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>天亮按钮框架dn frame
        dn = Frame()
        # 警长竞选提示label
        Label(dn, text='警长竞选').pack()
        # 查看死讯按钮
        Button(dn, text='查看死讯', command=self.dead_msg).pack()
        # 查看身份按钮
        Button(dn, text='查看身份', command=self.role_lst).pack()
        # 放置dn框架
        dn.pack()

    def dead_msg(self):
        # 死亡序列为空则为平安夜
        if self.Today_dead == []:
            messagebox.showinfo('今晚死讯', '今晚平安夜！')
        # 死亡序列不为空则宣布死讯
        else:
            messagebox.showinfo('今晚死讯', '今晚死亡的是：%s' %
                                str(self.Today_dead)[1:-1])

    # 角色信息展示
    def role_lst(self):
        if self.Farseer_in == 1:
            self.Player_role[self.Farseer_num - 1] = '预言家'
        if self.Guard_in == 1:
            self.Player_role[self.Guard_num - 1] = '守卫'
        if self.Wizard_in == 1:
            self.Player_role[self.Wizard_num - 1] = '女巫'
        # 生成玩家身份信息
        i = 1
        txt = ''
        while i <= self.Player_num:
            txt = txt + '%d号玩家：%s。\n' % (i, self.Player_role[i - 1])
            i += 1
        messagebox.showinfo('身份信息', txt)


if __name__ == '__main__':
    app1 = main()
    app1.master.title('Welcome Werewolf')
    app1.master.iconbitmap(r"werewolf.ico")
    app1.mainloop()
