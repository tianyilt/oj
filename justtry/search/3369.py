

# Adjusted sample input as per the provided input adjustments
SAMPLE_INPUT = """11
5 2
2 3
3 4
3 1
6 7
6 8
7 6
8 9
9 11
9 10
"""

# Convert SAMPLE_INPUT into an iterator of lines to simulate input function
def mock_input(s):
    it = iter(s.splitlines())
    return lambda: next(it, '')

input = mock_input(SAMPLE_INPUT)


from collections import defaultdict
# Initialize the graph
graph = defaultdict(list)
n = int(input())  # Number of nodes

# Fill the graph with edges
for _ in range(n-1):
    i, j = map(int, input().split())
    # Add edge in both directions to represent an undirected graph
    graph[i].append(j)
    graph[j].append(i)

def dfs(node, parent, depth):
    """
    Perform a depth-first search to count the number of paths of exactly 3 edges
    """
    if depth == 3:
        # A path of exactly 3 edges found
        return 1
    count = 0
    for neighbor in graph[node]:
        if neighbor != parent:
            # Recur for all neighbors except the parent
            count += dfs(neighbor, node, depth + 1)
    return count

# Start DFS from every node and accumulate paths of length 3
total_paths = sum(dfs(node, -1, 0) for node in range(1, n + 1)) // 2  # Divide by 2 to avoid counting reversed paths twice

print(total_paths)
