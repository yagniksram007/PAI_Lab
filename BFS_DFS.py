from collections import deque

def bfs(v):
    global n
    q = deque()
    q.append(v)
    visited = [0] * (n + 1)
    visited[v] = 1
    while q:
        u = q.popleft()
        for i in range(1, n + 1):
            if a[u][i] and not visited[i]:
                q.append(i)
                visited[i] = 1
                print(f"->{i}", end=' ')

def dfs(v):
    global n
    reach = [0] * (n + 1)
    reach[v] = 1
    for i in range(1, n + 1):
        if a[v][i] and not reach[i]:
            print(f"->{i}", end=' ')
            dfs(i)

if __name__ == "__main__":
    n = int(input("Enter the number of officers: "))
    a = [[0] * (n + 1) for _ in range(n + 1)]
    
    print("Enter graph data in matrix form indicating people who can communicate directly with each other:")
    for i in range(1, n + 1):
        a[i][1:] = map(int, input().split())

    v = int(input("Enter the officer as a starting node: "))
    if not (1 <= v <= n):
        print("Invalid node")
    else:
        print(f"All the officers which are reachable from a given officer as a starting node using BFS algorithm\n {v}", end=' ')
        bfs(v)
        print(f"\nAll the officers which are reachable from a given officer as a starting node using DFS algorithm\n {v}", end=' ')
        dfs(v)
        print()
