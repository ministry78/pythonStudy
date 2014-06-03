# -*- coding: UTF-8 -*-
__author__ = 'drudy'
"""这是nester.py模块，提供一个名为print_list()的函数，这个函数的功能是打印列表
    其中有可能包含（也可能不包含）嵌套列表
"""
def print_list(the_list):
"""这个函数取一个位置函数，名为the_list,这可以是任何python列表。所指定的列表中的每个数据项会输出到屏幕上，各数据各占一行"""
    for list1 in the_list:
        if isinstance(list1,list):
            print_list(list1)
        else:
            print(list1)
movies = ["龙珠","火影忍者","死神","海贼王",
    ["尾田",
        ["路飞","娜美"]]]
print_list(movies)
