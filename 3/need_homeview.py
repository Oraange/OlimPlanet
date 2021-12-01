# 많이 생각하고 시도해 보았으나 풀지 못하였습니다.
# DFS와 그래프 둘 중 하나로 풀어야 한다고 생각했지만 해결하지 못하였습니다.


'''
from math import inf
from sys import stdin

n = int(input())

cost = [[0] * n for _ in range(n)]
visited = [False] * n
answer = inf

for r in range(n):
    cost[r] = list(map(int,stdin.readline().split()))

def dfs(start):
    stack = []
    stack.append(start)

    while stack:
        cur = stack.pop()
        if not visited[cur]:
            visited[cur] = True
'''