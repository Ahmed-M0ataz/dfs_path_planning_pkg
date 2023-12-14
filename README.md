# Depth-First Search (DFS)

Depth-First Search (DFS) is similar to BFS, but with a key difference. While BFS explores all nodes around the start node before backtracking, DFS explores all branches in the first direction (node) before moving on to the next node. This distinction can be better understood in terms of nodes and grid maps.

## Node Perspective

- **BFS:** Searches all around the start node before returning to the first node.
- **DFS:** Searches all branches in the first direction (node) before moving to the next node.

## Grid Map Perspective

Here is a visual representation of the output for DFS compared to BFS:
![DFS Visualization](path/to/dfs_image.png) vs ![BFS Visualization](path/to/bfs_image.png)

In the same start and end configuration, DFS takes 7 iterations to reach the goal, while BFS takes 13 iterations. The efficiency depends on the start and goal locations. In some cases, BFS may be better, but in most cases, DFS is more efficient.

To run DFS on nodes, use the following command:

```bash
rosrun bfs_path_planning_pkg dfs_algorithm.py
