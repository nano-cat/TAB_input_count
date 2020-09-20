#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    通过统计TAB键的次数推测发送了多少条消息
    version: 0.1
    待更新: 存取结果 + GUI界面
"""
__author__ = "nano-cat"

import winput
import time

def keyboard_callback(event):
    global key_tab_num
    global send_massage_num

    if str(event.action) == "256":              # 判断按键是否是按下
        if event.vkCode == winput.VK_TAB:       #
            key_tab_num = key_tab_num + 1
            if (key_tab_num % 2) == 0:          # 按两次tab说明我发送一条消息
                send_massage_num = send_massage_num + 1
                print( time.strftime("%H:%M:%S", time.localtime()),"发送了一条消息\n")
        
        if event.vkCode == winput.VK_NEXT:      # 按Page Down 显示统计结果
            print("截至",time.strftime("%H:%M:%S", time.localtime()),"共发送了 %d 条消息\n" % send_massage_num)

        if event.vkCode == winput.VK_PRIOR:     # 按Page Up 退出
            print("关闭hook并退出")
            winput.stop()


if __name__ == "__main__":
    key_tab_num = 0
    send_massage_num = 0

    print("********************************")
    print("* 统计发送了多少条消息的小程序 *")
    print("*     --统计规则:              *")
    print("*        每两次tab发送一条消息 *")
    print("*                              *")
    print("* Page Down: 显示统计结果      *")
    print("* page Up:   退出程序          *")
    print("********************************")
    print("\n")

    # **

    # HOOK 输入
    winput.hook_keyboard(keyboard_callback)

    # 进入消息循环
    winput.wait_messages()

    # remove
    winput.unhook_keyboard()

