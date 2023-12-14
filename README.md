# Depth-First Search (DFS)

Depth-First Search (DFS) is similar to BFS, but with a key difference. While BFS explores all nodes around the start node before backtracking, DFS explores all branches in the first direction (node) before moving on to the next node. This distinction can be better understood in terms of nodes and grid maps.

For a detailed explanation of Breadth-First Search (BFS), refer to the following [BFS](https://github.com/Ahmed-M0ataz/bfs_path_planning_pkg) where BFS is explained.

## Node Perspective

- **BFS:** Searches all around the start node before returning to the first node.
- **DFS:** Searches all branches in the first direction (node) before moving to the next node.
## Node Perspective
![Node Visualization](https://github.com/Ahmed-M0ataz/dfs_path_planning_pkg/blob/main/media/tree-dfs-vs-bfs.gif)
## Grid Map Perspective
![grid Visualization](https://github.com/Ahmed-M0ataz/dfs_path_planning_pkg/blob/main/media/bfs_vs_dfs_grid.gif)

Here is a visual representation of the output for DFS compared to BFS:
![DFS Visualization](https://github.com/Ahmed-M0ataz/dfs_path_planning_pkg/blob/main/media/dfs_output.png) vs ![BFS Visualization](https://github.com/Ahmed-M0ataz/dfs_path_planning_pkg/blob/main/media/output_bfs.png)

In the same start and end configuration, DFS takes 7 iterations to reach the goal, while BFS takes 13 iterations. The efficiency depends on the start and goal locations. In some cases, BFS may be better, but in most cases, DFS is more efficient.

To run DFS on nodes, use the following command:

```bash
rosrun bfs_path_planning_pkg dfs_algorithm.py
