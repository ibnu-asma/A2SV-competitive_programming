# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
      
        if len(grid)==1 and len(grid[0])==1:
            return 0
        
        row , col = len(grid) , len(grid[0])
        visited = set()   
        
        hp = [] 
        
        visited.add((0,0))
        i,j = 0,0  
 
        ans = 0
        while (i,j) != (row-1,col-1):
          
            if i+1<row and (i+1,j) not in visited:
                d = abs(grid[i][j]-grid[i+1][j])
                heapq.heappush(hp,[d,i+1,j])
           
            if i-1>=0 and (i-1,j) not in visited:
                d = abs(grid[i][j]-grid[i-1][j])
                heapq.heappush(hp,[d,i-1,j])
          
            if j+1<col and (i,j+1) not in visited:
                d = abs(grid[i][j+1]-grid[i][j])
                heapq.heappush(hp,[d,i,j+1])
       
            if j-1>=0 and (i,j-1) not in visited:
                d = abs(grid[i][j-1]-grid[i][j])
                heapq.heappush(hp,[d,i,j-1])

            d,p,q = heapq.heappop(hp)

            ans = max(ans,d) 
            visited.add((p,q))
        
            i,j = p,q 
        return ans    