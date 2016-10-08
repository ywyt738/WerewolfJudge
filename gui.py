# -*- coding: utf-8 -*-
'''
这是一个狼人杀首夜法官工具GUI版本
版本:Ver0.6.0
支持角色：女巫，预言家，守卫
'''


from tkinter import *
import tkinter.messagebox as messagebox
import winsound

__author__ = 'HuangXiaojun'


class role_select(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.frm_top()
        self.frm_bottom()
        self.go = Button(self, text='开始游戏', command=self.start).pack()
        self.pack()

    def frm_top(self):
        self.frm_t = Frame()
        self.player_num = IntVar()
        self.werewolf_num = IntVar()
        self.msg_label = Label(
            self.frm_t, text='请选择游戏人数，最多12人：').pack()
        self.scale = Scale(self.frm_t, from_=5, to=12,
                           resolution=1, orient='horizontal', variable=self.player_num,).pack()
        self.msg_label2 = Label(
            self.frm_t, text='请选择狼人数量：').pack()
        self.scale2 = Scale(self.frm_t, from_=1, to=11,
                            resolution=1, orient='horizontal', variable=self.werewolf_num).pack()
        self.frm_t.pack()

    def frm_bottom(self):
        self.frm_b = Frame()
        self.farseer_in = IntVar()
        self.wizard_in = IntVar()
        self.guard_in = IntVar()
        self.wizard_saveself = IntVar()

        self.role1 = Checkbutton(
            self.frm_b, text='预言家', variable=self.farseer_in).grid(row=1, column=0)
        self.role3 = Checkbutton(
            self.frm_b, text='守卫', variable=self.guard_in).grid(row=1, column=1)
        self.role2 = Checkbutton(
            self.frm_b, text='女巫', variable=self.wizard_in).grid(row=2, column=0)
        self.nosaveself = Radiobutton(
            self.frm_b, text='不能自救', variable=self.wizard_saveself, value=0, state=DISABLED).grid(row=2, column=1)
        self.saveself = Radiobutton(
            self.frm_b, text='能自救', variable=self.wizard_saveself, value=1, state=DISABLED).grid(row=2, column=2)
        self.frm_b.pack()

    def start(self):
        join = {1: '有', 0: '无'}
        can = {1: '能', 0: '不能'}
        self.farseer = self.farseer_in.get()
        self.wizard = self.wizard_in.get()
        self.guard = self.guard_in.get()
        self.Player_num = self.player_num.get()
        self.Werewolf_num = self.werewolf_num.get()
        self.Wizard_saveself = self.wizard_saveself.get()
        messagebox.showinfo('游戏配置', '''
        玩家一共%d人，狼人%d人。
        预言家：%s
        女巫：%s。女巫%s自救。
        守卫：%s
        ''' % (self.Player_num, self.Werewolf_num, join[self.farseer], join[self.wizard], can[self.Wizard_saveself], join[self.guard]))
        self.Player_role = ['村民'] * self.Player_num  # 生成玩家身份序列
        self.today_dead = []  # 生成死亡玩家序列

        self.frm_t.destroy()
        self.frm_b.destroy()
        self.destroy()
        self.ww()

    def ww(self):
        wav_start = r".\audio\werewolf_st.wav"
        winsound.PlaySound(wav_start, winsound.SND_NODEFAULT)

        self.killed_num = IntVar()

        self.ww = Frame()
        self.msg_label = Label(
            self.ww, text='狼人请选择你们的号码：').pack()
        self.adict = {}
        for i in list(range(self.Player_num)):
            self.adict['a' + str(i)] = IntVar()
        for i in range(self.Player_num):
            Checkbutton(self.ww, text=i + 1, onvalue=i + 1,
                        variable=self.adict['a' + str(i)]).pack(side="left")
        self.ww.pack()

        self.ww1 = Frame()
        Label(self.ww1, text='狼人请选择要击杀的目标(0为空刀)：').pack()
        for r in range(self.Player_num + 1):
            Radiobutton(self.ww1, text=r, value=r,
                        variable=self.killed_num).pack(side='left')
        self.ww1.pack()
        self.ww2 = Frame()
        Button(self.ww2, text='确定', command=self.ww_go).pack()
        self.ww2.pack()

    def ww_go(self):
        ww_list = []
        for i in range(self.Player_num):
            a = self.adict['a' + str(i)].get()
            if a != 0:
                ww_list.append(a)
        self.killed_player = self.killed_num.get()
        self.wwteam = ww_list
        if self.killed_player == 0:
            pass
        else:
            self.today_dead.append(self.killed_player)
        for i in self.wwteam:
            self.Player_role[int(i) - 1] = '狼人'
        msg_ww_team = str(ww_list)[1:len(str(ww_list)) - 1]
        messagebox.showinfo('狼人阶段信息', '''
        狼队：%s。
        今晚你们要击杀的是%s号''' % (msg_ww_team, self.killed_player))
        wav_finish = r".\audio\werewolf_fi.wav"
        winsound.PlaySound(wav_finish, winsound.SND_NODEFAULT)
        self.ww.destroy()
        self.ww1.destroy()
        self.ww2.destroy()
        if self.farseer == 1:
            self.fse()
        elif self.guard == 1:
            self.grd()
        elif self.wizard == 1:
            self.wzd()
        else:
            self.dawn()

    def fse(self):
        wav_start = r".\audio\farseer_st.wav"
        winsound.PlaySound(wav_start, winsound.SND_NODEFAULT)  # 唤醒预言家
        self.farseer_num = IntVar()
        self.check_num = IntVar()
        self.fe = Frame()
        Label(self.fe, text='预言家输入你的号码：').pack()
        for r in range(1, self.Player_num + 1):
            Radiobutton(self.fe, text=r, value=r,
                        variable=self.farseer_num).pack(side='left')
        self.fe.pack()
        self.fe1 = Frame()
        Label(self.fe1, text='请输入你要查看的号码：').pack()
        for r in range(1, self.Player_num + 1):
            Radiobutton(self.fe1, text=r, value=r,
                        variable=self.check_num).pack(side='left')
        self.fe1.pack()
        self.fe2 = Frame()
        Button(self.fe2, text='确定', command=self.fse_go).pack()
        self.fe2.pack()

    def fse_go(self):
        messagebox.showinfo('验人结果', '你查看的人是：%d号。\n他是：%s。' % (
            self.check_num.get(), self.Player_role[self.check_num.get() - 1]))
        self.fe.destroy()
        self.fe1.destroy()
        self.fe2.destroy()
        wav_finish = r".\audio\farseer_fi.wav"
        winsound.PlaySound(wav_finish, winsound.SND_NODEFAULT)  # 预言家闭眼
        if self.guard == 1:
            self.grd()
        elif self.wizard == 1:
            self.wzd()
        else:
            self.dawn()

    def grd(self):
        wav_start = r".\audio\guard_st.wav"
        winsound.PlaySound(wav_start, winsound.SND_NODEFAULT)
        self.guard_num = IntVar()
        self.protect_num = IntVar()
        self.gd = Frame()
        Label(self.gd, text='守卫输入你的号码：').pack()
        for r in range(1, self.Player_num + 1):
            Radiobutton(self.gd, text=r, value=r,
                        variable=self.guard_num).pack(side='left')
        self.gd.pack()
        self.gd1 = Frame()
        Label(self.gd1, text='请输入你要保护的号码：').pack()
        for r in range(1, self.Player_num + 1):
            Radiobutton(self.gd1, text=r, value=r,
                        variable=self.protect_num).pack(side='left')
        self.gd1.pack()
        self.gd2 = Frame()
        Button(self.gd2, text='确定', command=self.grd_go).pack()
        self.gd2.pack()

    def grd_go(self):
        messagebox.showinfo('守卫信息', '今晚你保护的人是：%d号。' % (self.protect_num.get()))
        self.gd.destroy()
        self.gd1.destroy()
        self.gd2.destroy()
        wav_finish = r".\audio\guard_fi.wav"
        winsound.PlaySound(wav_finish, winsound.SND_NODEFAULT)
        if self.protect_num.get() == self.killed_player:
            self.killed_player = 0
            self.today_dead.pop()
        if self.wizard == 1:
            self.wzd()
        else:
            self.dawn()

    def wzd(self):
        wav_start = r".\audio\wizard_st.wav"
        winsound.PlaySound(wav_start, winsound.SND_NODEFAULT)
        self.wizard_num = IntVar()
        self.protect_num = IntVar()
        self.save = IntVar()
        self.wd = Frame()
        Label(self.wd, text='女巫输入你的号码：').pack()
        for r in range(1, self.Player_num + 1):
            Radiobutton(self.wd, text=r, value=r,
                        variable=self.wizard_num).pack(side='left')
        self.wd.pack()
        self.wd1 = Frame()
        Label(self.wd1, text='今天晚上%s号死了。你是否要救？是否要用毒药？' %
              self.killed_player).pack()
        Radiobutton(self.wd1, text='救', value=0,
                    variable=self.save).pack(side='left')
        for r in range(1, self.Player_num + 1):
            Radiobutton(self.wd1, text=r, value=r,
                        variable=self.save).pack(side='left')
        self.wd1.pack()
        self.wd2 = Frame()
        Radiobutton(self.wd2, text='解药、毒药都不用。',
                    value=99, variable=self.save).pack()
        Button(self.wd2, text='确定', command=self.wzd_go).pack()
        self.wd2.pack()

    def wzd_go(self):
        wav_finish = r".\audio\wizard_fi.wav"
        if self.save.get() == 0:
            self.today_dead.pop()
            messagebox.showinfo('女巫信息','今天晚上%s号死了，你解救了他/她。' % self.killed_player)
        elif self.save.get() != 99:
            self.today_dead.append(self.save.get())
            messagebox.showinfo('女巫信息','今天晚上%s号死了，你没有使用解药，并且你下毒杀死了%s号' % (self.killed_player, self.save.get()))
        elif self.save.get() == 99:
            messagebox.showinfo('女巫信息','今天晚上%s号死了，你没有使用解药和毒药。'% self.killed_player)
        winsound.PlaySound(wav_finish, winsound.SND_NODEFAULT)
        self.wd.destroy()
        self.wd1.destroy()
        self.wd2.destroy()
        self.dawn()

    def dawn(self):
        wav_dawn = r".\audio\dawn.wav"
        winsound.PlaySound(wav_dawn, winsound.SND_NODEFAULT)  # 天亮
        self.dn = Frame()
        Label(self.dn, text='警长竞选').pack()
        Button(self.dn, text='查看死讯', command=self.dead_msg).pack()
        Button(self.dn, text='查看身份', command=self.role_lst).pack()
        self.dn.pack()

    def dead_msg(self):
        if self.today_dead == []:
            messagebox.showinfo('今晚死讯', '今晚平安夜！')
        else:
            self.today_dead.sort()
            msg_dead = str(self.today_dead)[1:len(str(self.today_dead))-1]
            messagebox.showinfo('今晚死讯', '今晚死亡的是：%s' % msg_dead)

    def role_lst(self):
        if self.farseer == 1:
            self.Player_role[self.farseer_num.get() - 1] = '预言家'
        if self.guard == 1:
            self.Player_role[self.guard_num.get() - 1] = '守卫'
        if self.wizard == 1:
            self.Player_role[self.wizard_num.get() - 1] = '女巫'
        i = 1
        txt = ''
        while i <= self.Player_num:
            txt = txt + '%d号玩家：%s。\n' % (i, self.Player_role[i - 1])
            i += 1
        messagebox.showinfo('身份信息', txt)

start = Tk()
app1 = role_select(master=start)
app1.master.title('Welcome Werewolf')
app1.mainloop()
