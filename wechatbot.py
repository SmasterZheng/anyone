# -*- coding: UTF-8 -*-
from wxpy import *
bot = Bot(cache_path=True)
# 启用聊天对象的puid属性
bot.enable_puid()
# 启用图灵机器人
tuling = Tuling(api_key='2260a07d0980473c8a60ec54561f3b8b')
# 打印所有收到的消息
@bot.register()
def print_others(Message):
    print(Message)
# 设置群聊中@回复
@bot.register(Group, TEXT)
def print_group_msg(Message):
    # if Message.is_at:
    print(Message)
    tuling.do_reply(Message)
# 堵塞线程防止程序退出
bot.join()
embed()