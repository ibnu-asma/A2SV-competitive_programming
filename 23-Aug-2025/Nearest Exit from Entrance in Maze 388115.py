# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n = len(maze),len(maze[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        q = deque([entrance])
        
        visited = {tuple(entrance)}
        
        steps = 0
        while q:
            
            for _ in range(len(q)):
                xo,yo = q.popleft()
                if (0 in [xo,yo] or xo==m-1 or yo==n-1) and [xo,yo]!=entrance:
                    return steps
                for xn,yn in directions:
                    x,y = xo+xn,yo+yn
                    if 0<=x<m and 0<=y<n and maze[x][y]=='.' and (x,y) not in visited:
                        visited.add((x,y))
                        q.append([x,y])
            steps += 1
        
        return -1