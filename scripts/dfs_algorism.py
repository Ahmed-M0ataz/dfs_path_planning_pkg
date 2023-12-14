#!/usr/bin/env python

import numpy as np

R, C = 5, 5
m = [['S', '.', '', '#', '.'],
     ['.', '#', '.', '.', 'E'],
     ['.', '#', '.', '#', '.'],
     ['.', '.', '.', '.', '#'],
     ['#', '.', '#', '.', '.']]

sr, sc = 0, 0
e = (0, 0)

stack = []  # Using a stack for DFS
visited = np.zeros((5, 5))
prev = np.zeros((5, 5), dtype=tuple)

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

cells_searched = 0  # Counter for the number of cells searched

def explore_neighbours(r, c):
    global prev, cells_searched
    for i in range(4):
        rr, cc = r + dr[i], c + dc[i]
        if 0 <= rr < R and 0 <= cc < C and not visited[rr][cc] and m[rr][cc] != '#':
            stack.append((rr, cc))
            visited[rr][cc] = True
            prev[rr][cc] = (r, c)
            cells_searched += 1  # Increment the cell search count

def dfs_solve():
    global e, prev
    visited[sr][sc] = True
    stack.append((sr, sc))

    while stack:
        r, c = stack.pop()

        if m[r][c] == 'E':
            e = (r, c)
            break

        explore_neighbours(r, c)

    return e

def get_shortest_path(prev, s):
    global e
    path = []
    at = e

    while at != 0.0:
        path.append(at)
        at = prev[at[0]][at[1]]

    path.reverse()

    if path[0] == s:
        return path
    return []

dfs_solve()

shortest_path = get_shortest_path(prev, (sr, sc))
prev[sr][sc] = 'S'
prev[e[0]][e[1]] = 'E'
print(f"Final visited: \n{visited} \n")
print(f"Matrix  final track path: \n{prev} \n")
print("Shortest path indexing:", shortest_path)
print("Number of cells searched to reach the goal:", cells_searched)
