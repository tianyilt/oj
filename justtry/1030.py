#https://acm.ecnu.edu.cn/problem/1030/
def mock_input(s):
    """
    返回一个函数，该函数每次被调用时，会返回输入字符串中的下一行。
    """
    it = iter(s.splitlines())
    return lambda: next(it)

# 样例输入
SAMPLE_INPUT = """1
4
5
9
20
0
"""

# 替换 input 函数
input = mock_input(SAMPLE_INPUT)


# nn = [1,2,3,4,5]
def next_year(nn):
    res = [0]*(len(nn)+1)
    for i in range(len(nn)+1):
        if i ==0:
            res[i]=0
            continue
        res[i]=nn[i-1]

        if i>2:
            res[0]+=nn[i-1]
        
    return res
# next_year(nn)


all =[[1]]
while True:
    try:
        N = int(input())
        if N == 0:
            break
        # print(N, len(all))
        if N >len(all):
            for i in range(len(all),N):
                # print(i, all)
                all.append(next_year(all[i-1]))
        # else:
        #     res = sum(all[N])
        # print(all)
        res = sum(all[N-1])
        print(res)
        
        
        # nn = [1]
        # for i in range(N):
        #     nn = next_year(nn)
        #     print(i+2,nn)
        # res = sum(nn)
        # print(res)
        
        
 
    except:
        break