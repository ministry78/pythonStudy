#coding=utf-8
movies = ["龙珠","火影忍者","死神","海贼王",
    ["尾田",
        ["路飞","娜美"]]]
# print(movies[0])
# movies.append("喜羊羊")
# print(movies)
# movies.pop()
# movies.extend(["圣斗士","猎人"])
# movies.remove("圣斗士")
# movies.insert(0,"灌篮高手")
print(len(movies))
# print(movies)
#---------------------------------------
# for list1 in movies:
#     if isinstance(list1,list):
#         for inlist in list1:
#             if isinstance(inlist,list):
#                 for inlist2 in inlist:
#                     print(inlist2)
#             else:
#                 print(inlist)
#     else:
#         print(list1)
#---------------------------------------
def print_list(the_list):
    for list1 in the_list:
        if isinstance(list1,list):
            print_list(list1);
        else:
            print(list1)
print_list(movies)