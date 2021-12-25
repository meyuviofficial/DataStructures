class Solution:
    def isValid(self, grid: List[List[str]], i: int, j: int, isVisited: List[List[bool]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if ((i >= 0 and i < m) and (j >= 0 and j < n) and (isVisited[i][j] == False and grid[i][j] == "1")):
            return True
        return False

    def DFS(self, grid: List[List[str]], i: int, j: int, isVisited: List[List[bool]]):
        isVisited[i][j] = True
        rowTraversal = [-1, 0, 0, 1]
        colTraversal = [0, -1, 1, 0]

        for k in range(len(rowTraversal)):
            if self.isValid(grid, i+rowTraversal[k], j+colTraversal[k], isVisited):
                self.DFS(grid, i+rowTraversal[k], j+colTraversal[k], isVisited)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        isVisited = [[False for y in range(n)] for x in range(m)]
        for i in range(m):
            for j in range(n):
                if isVisited[i][j] == False and grid[i][j] == "1":
                    self.DFS(grid, i, j, isVisited)
                    count += 1

        return count

"""
Example 1:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Example 2:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""