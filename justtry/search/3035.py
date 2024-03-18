# https://acm.ecnu.edu.cn/problem/3035/

def mock_input(s):
    """
    返回一个函数，该函数每次被调用时，会返回输入字符串中的下一行。
    """
    it = iter(s.splitlines())
    return lambda: next(it)

# 样例输入
SAMPLE_INPUT = """3
2 3
1 1 0
0 1 1
4 5
0 1 1 0 1
0 0 0 1 0
0 1 1 1 0
0 1 0 0 0
5 6
1 1 0 0 1 1
1 1 0 1 1 0
0 0 1 0 0 1
1 1 0 1 0 1
0 1 0 1 1 0
"""

# 替换 input 函数
input = mock_input(SAMPLE_INPUT)

from typing import List
from collections import deque

def BFS(im: List[List[int]], x, y, visited: List[List[int]]):
    if im[x][y]==0 or visited[x][y]==True:
        return 0
    q = deque([(x,y)])
    area = 0
    
    while q:
        cx,cy = q.popleft()
        for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx,ny = cx+dx,cy+dy
            # print(nx,ny,len(im),len(im[0]))
            if not (nx<len(im) and nx>=0 and ny<len(im[0]) and ny>=0):
                continue
            if not visited[nx][ny] and im[nx][ny]==1:
                visited[nx][ny]=True
                area +=1
                q.append((nx,ny))
    
    return area


T = int(input())

for t in range(T):
    n,m = map(int, input().split())
    visited = [[False for _ in range(m)] for _ in range(n)]
    im = []
    for nn in range(n):
        row = map(int, input().split())
        im.append(list(row))
    
    res_set = set()
    for x in range(n):
        for y in range(m):
            if im[x][y]==0 or visited[x][y]==True:
                continue
            res_set.add(BFS(im,x,y,visited))
    
    res_list = list(res_set)
    if len(res_list)<2:
        res = 0
    else:
        res_list.sort()
        res = res_list[-2]
    # print(res_set)
    
    
    # res = 0
    print(f"case #{t}:\n{res}")