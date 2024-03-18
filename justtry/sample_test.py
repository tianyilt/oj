#https://blog.csdn.net/qq_42685969/article/details/82085067
import sys
for line in sys.stdin:
    a = line.split()

input = "hello world"



a=input.split(" ")
print(len(a[-1]))

"""3.明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤1000），对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据，希望大家能正确处理)。
————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。
                        
原文链接：https://blog.csdn.net/qq_42685969/article/details/82085067
    """
nlist= []
while True:
    try:
        n = int(input())
        res = set()
        for i in range(n):
            res.add(int(input()))
        for i in sorted(res):
            print(i)
    except:
        break
nlist.sort(reverse=True)

"""
4.• 连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
• 长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
"""

a= "2345678901234567890"
a="1"
times=len(a)//8
yushu = len(a) % 8
res=[]
for t in range(times):
    res.append(a[8*t:8*t+8])
if yushu>0:
    res.append(a[times*8:]+(8-yushu)*"0")
print(res)

while True:
    try:
        print(int(input(),16))
    except:
        break