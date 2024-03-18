#https://acm.ecnu.edu.cn/problem/3241/
def mock_input(s):
    """
    返回一个函数，该函数每次被调用时，会返回输入字符串中的下一行。
    """
    it = iter(s.splitlines())
    return lambda: next(it)

# 样例输入
SAMPLE_INPUT = """3
EWRDFDdfldfke
213233439849384934
?DF":*(**^&WEqweWE
"""

# 替换 input 函数
input = mock_input(SAMPLE_INPUT)

T = int(input())

for t in range(T):
    st = input()
    res = ""
    for i,a in enumerate(st):
        if not a.isalpha():
            res = res+a
            continue
        if i % 2 ==0:
            res= res + a.lower()
        else:
            res = res+ a
    print(f"case #{t}:")
    print(res)