# 输入处理
测试
``` python
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
```
输入处理
```python
T = int(input())
c, w = map(int, input().split())
while True:
    try:
        
    except:
        break
```

# vscode常用快捷键
alt 上 移动当前行
ctrl d 光标跳转到多个重复的字符实现多行编辑

# 常用初始化

```python
n,m = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
```

# search

BFS
`deque`（双端队列）是Python中collections模块提供的一个高效的数据结构，它支持从两端以近乎常数时间复杂度进行添加和删除操作。在算法题和编程挑战中，`deque`可以用于多种场景，其中几个常见的用法包括：

### 1. 实现队列和栈
由于`deque`支持从两端进行操作，它既可以作为一个队列（先入先出，FIFO）也可以作为一个栈（后入先出，LIFO）使用。这使得`deque`成为实现广度优先搜索（BFS）或深度优先搜索（DFS）等算法时的理想选择。

- **作为队列**：用于BFS算法，使用`append()`方法从一端添加元素，使用`popleft()`方法从另一端移除元素。
- **作为栈**：用于DFS算法，使用`append()`方法添加元素，使用`pop()`方法移除元素，都在同一端进行。

### 2. 滑动窗口
在处理需要维护一定范围内元素的算法问题时，如计算滑动窗口的最大值或最小值，`deque`可以有效地存储当前窗口中的候选元素。通过保持`deque`中元素的递增或递减顺序，可以确保窗口中的最大或最小元素始终可在`O(1)`时间内访问。

### 3. 循环队列
对于需要循环利用空间的场景，如缓冲区管理，`deque`的两端操作特性使其成为实现循环队列的理想选择。可以通过限制`deque`的大小并从一端添加元素，从另一端移除元素来模拟循环队列的行为。

### 4. 回文字符串检查
利用`deque`的两端操作，可以高效地从两端同时比较字符串中的字符，以检查字符串是否为回文。

### 示例代码片段

**实现BFS算法：**
```python
from collections import deque

graph={ 0:[1,3,4], 1:[0,2,4], 2:[1,6], 3:[0,4,6], 4:[0,1,3,5], 5:[4], 6:[2,3] }

def bfs(graph, start, path=[]):
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in path:
            path.append(vertex)
            queue.extend(set(graph[vertex]).difference(path))
            # queue.extend(node for node in graph[vertex] if node not in path)
            # queue.extend(set(graph[vertex]) - set(path))
    return path

print bfs(graph, 0)
```

**滑动窗口最大值：**
```python
from collections import deque

def maxSlidingWindow(nums, k):
    deq = deque()
    result = []
    for i in range(len(nums)):
        while deq and deq[0] < i - k + 1:
            deq.popleft()
        while deq and nums[i] >= nums[deq[-1]]:
            deq.pop()
        deq.append(i)
        if i >= k - 1:
            result.append(nums[deq[0]])
    return result
```

`deque`在算法题中的应用非常广泛，上述只是几个例子。熟悉`deque`的各种操作能够帮助你在解决问题时更加灵活和高效。

```python
# 函数用于执行BFS并计算连通区域的面积
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
```

## DFS
深度优先搜索（DFS）是一种用于遍历或搜索树或图的算法。它从一个起点出发，探索尽可能深的分支，直到到达终点，然后回溯到前一个分叉点，探索未被探索的分支。DFS可以递归实现，也可以用栈来实现非递归版本。

以下是使用递归方式实现DFS的Python示例，这个例子中我们将使用DFS来遍历一个图，并打印每个节点：

### 示例：递归实现DFS

假设我们有一个图，表示为邻接列表：

```python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
```

这里的图是无向的，字典的键是图中的节点，值是与这些节点相连的节点列表。

我们将实现一个`dfs`函数，它接受图、当前节点和一个集合来记录已访问的节点：

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]  # 使用列表作为栈
    while stack:  # 当栈不为空时继续循环
        node = stack.pop()  # 弹出栈顶元素
        if node not in visited:
            print(node)
            visited.add(node)
            # 将邻居节点添加到栈中，注意这里添加顺序的不同可能会导致遍历顺序的变化
            stack.extend([n for n in graph[node] if n not in visited])
    return visited

# 调用非递归的DFS
dfs_iterative(graph, 'A')
```

在这个非递归版本中，我们使用栈来存储即将访问的节点，这样可以模拟递归过程中的调用栈。每次从栈中取出一个节点来访问，并将其未访问的邻居节点加入栈中。

这两种方法都是实现DFS的有效方式，具体使用哪一种取决于问题的需求和个人偏好。

# python 常见数据结构

在解决Python算法题时，理解和合理应用Python内置的数据结构是非常关键的。这不仅能帮助你更高效地解决问题，还能让你的代码更加简洁易读。以下是一些常见数据结构的中文介绍，以及它们在具体算法题中的应用例子：

## 1. **字典（`dict`）**
字典用于存储键值对，适用于需要快速查找、插入和删除的场景。例如，在一个字符串中统计每个单词出现的次数，可以使用字典来实现：

```python
def count_words(s):
    words = s.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
```

在LeetCode或任何算法编程挑战中，字典（`dict`）是Python中非常有用的数据结构之一，主要因为其键值对存储机制和高效的查找时间复杂度（平均情况下为O(1)）。以下是一些在解决算法问题时常用的字典用法：

d 就是一个字典，其中 get(key, default) 函数可以通过 key 从 d 中找出对应的值，如果 key 不存在则返回默认值 default


### 1. 计数

字典常用于元素计数。可以用来统计数组或字符串中元素的频率。

```python
from collections import Counter
nums = [1, 2, 2, 3, 3, 3]
count = Counter(nums)  # 或者使用手动循环来更新字典
# count = {1: 1, 2: 2, 3: 3}
```

### 2. 哈希表实现

字典在实现哈希表时非常有用，用于快速查找、插入和删除操作。

```python
hash_table = {}
hash_table['key1'] = 'value1'
hash_table['key2'] = 'value2'
```

### 3. 存储图

字典可以用来表示图，键为节点，值为与该节点相邻的节点列表。

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
```

### 4. 缓存（Memoization）

在递归算法中，字典用作缓存来存储已解决子问题的结果，这是动态规划和减少计算重复的常用技术。

```python
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```

### 5. 映射关系

字典可以存储一对一或一对多的映射关系，比如用户ID到用户名的映射。

```python
user_id_to_name = {1: 'Alice', 2: 'Bob', 3: 'Charlie'}
```

### 6. 默认字典（`defaultdict`）

`defaultdict`是`collections`模块中的一个子类，它提供了所有字典方法，并接受一个第一参数来指定字典值的默认数据类型。

```python
from collections import defaultdict
dd = defaultdict(list)
dd['key'].append(1)  # 不需要先检查key是否存在
```

### 7. 有序字典（`OrderedDict`）

`OrderedDict`是一个记住了元素添加顺序的字典。

```python
from collections import OrderedDict
od = OrderedDict()
od['z'] = 1
od['a'] = 2
od['b'] = 3
# Items will be printed in the order 'z', 'a', 'b'
```

字典的这些用法使其成为解决算法问题时的强大工具，不仅因为它们的灵活性和效率，还因为它们提供的丰富的内置方法和扩展库支持。


## 2. **集合（`set`）**
集合用于存储唯一元素，可以进行并集、交集、差集等操作。在需要去重或判断元素是否存在时非常有用。例如，从列表中移除重复元素：

```python
def remove_duplicates(lst):
    return list(set(lst))
```
存在性检查
集合在内部使用哈希表实现，所以查找元素（即判断一个元素是否属于某个集合）的时间复杂度是O(1)。这使得集合非常适合进行快速的存在性检查。

```python
Copy code
elements = set([1, 2, 3, 4, 5])
# 检查元素是否存在
if 3 in elements:
    print("3 exists in the set")
# 输出: 3 exists in the set
```


## 3. **列表（`list`）**
列表是Python中最基本的数据结构，用于存储有序集合。在需要按顺序存取元素或进行列表推导时非常有用。例如，生成一个列表的平方数列表：

```python
def square_list(lst):
    return [x**2 for x in lst]
```

## 4. **队列（`deque`）**
`deque`，即双端队列，是一种既可以从前端也可以从后端进行元素添加和移除的线性数据结构。在需要实现队列功能，特别是在广度优先搜索（BFS）算法中非常有用：

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited
```

## 5. **堆（`heapq`）**
堆是一种特殊的完全二叉树结构，常用于优先队列，如需要快速访问最小或最大元素的场景。例如，找到一个列表中的第K大元素：

```python
import heapq

def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]
```

## 链表
```python
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        p = dummy
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p = p1
                p1 = p1.next
            else:
                p.next = p2
                p = p2
                p2 = p2.next
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return dummy.next
```

test的方法
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node and a current node pointing to dummy
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists and compare each node
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach the remainder of list1 or list2
        current.next = list1 or list2

        # Return the merged list, skipping the dummy node
        return dummy.next

# Helper function to convert array to linked list
def arrayToList(arr):
    head = ListNode(0)
    current = head
    for number in arr:
        current.next = ListNode(number)
        current = current.next
    return head.next

# Helper function to print linked list
def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

# Test cases
solution = Solution()

# Convert arrays to linked lists
l1 = arrayToList([1,2,4])
l2 = arrayToList([1,3,4])

# Merge lists and print result
mergedList = solution.mergeTwoLists(l1, l2)
printList(mergedList)  # Expected output: 1 1 2 3 4 4

# Additional test cases
testCases = [
    ([], []),
    ([], [0])
]

for l1Arr, l2Arr in testCases:
    l1 = arrayToList(l1Arr)
    l2 = arrayToList(l2Arr)
    mergedList = solution.mergeTwoLists(l1, l2)
    printList(mergedList)

```