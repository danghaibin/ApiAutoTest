#!/usr/bin/env python3.8.5
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 16:34
# @Author  : Danghaibin
# @FileName: Monitor.py
# @Software: PyCharm
'''
监控代码  监控服务器的内存、cpu、网络、磁盘等。与租车系统部署在一起
'''
from datetime import datetime
from time import sleep
import psutil

# print(psutil.cpu_percent())  # 获取cpu信息
# print(psutil.virtual_memory())  # 虚拟内存
# print(psutil.virtual_memory().percent)  # 虚拟内存百分比
# print(psutil.disk_usage("d:/"))  # 租车系统所在磁盘
# print(psutil.disk_usage("d:/").percent)  # 租车系统所在磁盘的百分比
# print(psutil.net_io_counters())  # 网络
# print(psutil.net_io_counters().bytes_sent)  # 发送的字节数
# print(psutil.net_io_counters().bytes_recv)  # 接收的字节数

# 达到类似serveragent的效果 在性能测试期间 获取cpu、内存的趋势
# 设置死循环 每隔3秒读一次 把读的结果写到文件中 测试结束后分析文件 使用excel生成图标
# 时间戳 cpu% 内存% 磁盘% 发送字节数 接收字节数

with open('d:/资源占用情况.txt', encoding='utf-8', mode='a') as f:
    f.write("\t时间戳\t\tcpu%\t内存%\t磁盘%\t发送字节数\t接收字节数\n")
    while True:
        print("监控中......")
        # strftime
        f.write(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S") + "\t\t")
        f.write(str(psutil.cpu_percent()) + "%\t")
        f.write(str(psutil.virtual_memory().percent) + "%\t")
        f.write(str(psutil.disk_usage("d:/").percent) + "%\t")
        f.write(str(psutil.net_io_counters().bytes_sent) + "\t")
        f.write(str(psutil.net_io_counters().bytes_recv) + "\n")
        f.flush() # 从缓存刷新到文件中 避免文件没有关闭 之前的内容一直写不进去
        sleep(3)
