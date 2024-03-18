#https://acm.ecnu.edu.cn/problem/2971/
def mock_input(s):
    """
    返回一个函数，该函数每次被调用时，会返回输入字符串中的下一行。
    """
    it = iter(s.splitlines())
    return lambda: next(it)

# 样例输入
SAMPLE_INPUT = """2
2 8
3 1
"""

# 替换 input 函数
input = mock_input(SAMPLE_INPUT)

import sys
T = int(input())

for t in range(T):
    c, w = map(int, input().split())
    c = int(c)
    w = int(w)
    res = 0
    times = 1
    init=10**(c-1)+10**(c-1)%3
    while True:
        cur_num = init + (times-1)*3
        if (cur_num)< 10**c:
            if cur_num %10 ==w:
                res+=1
            times+=1
        else:
            break 
    print(f"case #{t}:")
    print(res)
