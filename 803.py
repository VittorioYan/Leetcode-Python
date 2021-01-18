from typing import List, Sequence
import collections
import bisect
# my solution
# class brick:
#     def __init__(self,isin) -> None:
#         super().__init__()
#         self.isin = isin
#         self.rely = set()

# class Solution:
#     def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
#         m,n = len(grid),len(grid[0])
#         visited = [[0]*n for _ in range(m)]
#         bricks = [[0]*n for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 bricks[i][j] = brick(grid[i][j])

#         def check(poi):
#             i,j = poi
#             if i<0 or j<0 or i>=m or j>=n or not bricks[i][j].isin:
#                 return False
#             return True

#         def construct(cur,from_poi):
#             i,j = cur
#             if not check(cur):
#                 return
#             visited[i][j] = 1
#             bricks[i][j].rely.add(from_poi)
#             next_pos = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
#             next_pos.remove(from_poi)
#             for item in next_pos:
#                 if check(item) and not visited[item[0]][item[1]]:
#                     construct(item,cur)
#         def drop(poi):
#             i,j = poi
#             if not check(poi):
#                 return 0
#             bricks[i][j].isin = 0
#             next_pos = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
#             result = 1
#             for item in next_pos:
#                 if not check(item):
#                     continue
#                 ni,nj = item
#                 if poi in bricks[ni][nj].rely:
#                     bricks[ni][nj].rely.remove(poi)
#                     if not bricks[ni][nj].rely:
#                         result+=drop(item)
#             return result
            

#         for j in range(n):
#             if grid[0][j]:
#                 visited = [[0]*n for _ in range(m)]
#                 construct((1,j),(0,j))
#         ans = []
#         for hit in hits:
#             ans.append(max(drop((hit[0],hit[1]))-1,0))
#             # for i in range(m):
#             #     for j in range(n):
#             #         print(bricks[i][j].isin)
#         return ans
#         # for i in range(m):
#         #     for j in range(n):
#         #         print(bricks[i][j].rely)

class UnionFind:
    def __init__(self):
        self.father = {}
        self.size_of_set = {}
    
    def get_size_of_set(self,x):
        """
        获取所在连通块的大小
        """
        return self.size_of_set[self.find(x)]
    
    def find(self,x):
        root = x
        
        while self.father[root] != None:
            root = self.father[root]
        
        # 路径压缩
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        
        return root
    
    def is_connected(self,x,y):
        return self.find(x) == self.find(y)
    
    def merge(self,x,y):
        root_x,root_y = self.find(x),self.find(y)
        
        if root_x != root_y:
            self.father[root_x] = root_y
            # 更新根节点连通块数量
            self.size_of_set[root_y] += self.size_of_set[root_x]
            del self.size_of_set[root_x]
    
    def add(self,x):
        if x not in self.father:
            self.father[x] = None
            self.size_of_set[x] = 1
            

class Solution:
    def __init__(self):
        self.CEIL = (-1,-1)
        self.DIRECTION = ((1,0),(-1,0),(0,1),(0,-1))
    
    def initialize(self,uf,m,n,grid,hits):
        """
        初始化
        """
        # 添加天花板
        uf.add(self.CEIL)
        
        # 敲掉所有要敲掉的砖块
        for x,y in hits:
            grid[x][y] -= 1
        
        # 连接，合并剩余的砖块
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    uf.add((i,j))
       
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.merge_neighbors(uf,m,n,grid,i,j)
        
        # 与天花板合并
        for j in range(n):
            if grid[0][j] == 1:
                uf.merge((0,j),self.CEIL)
    
    def is_valid(self,x,y,grid,m,n):
        return 0 <= x < m and 0 <= y < n and grid[x][y] == 1
    
    def merge_neighbors(self,uf,m,n,grid,x,y):
        """
        与上下左右的砖块合并
        """
        for dx,dy in self.DIRECTION:
            nx,ny = x+dx,y+dy
            if not self.is_valid(nx,ny,grid,m,n):
                continue
            uf.merge((x,y),(nx,ny))
    
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        uf = UnionFind()
        m,n = len(grid),len(grid[0])
        res = [0] * len(hits)
        
        # 初始化
        self.initialize(uf,m,n,grid,hits)

        for i in range(len(hits)-1,-1,-1):
            x,y = hits[i][0],hits[i][1]
            
            # 还原敲击
            grid[x][y] += 1
            
            # 敲的地方原本就不是砖块
            if grid[x][y] != 1:
                continue
            
            # 敲完以后与天花板连接的数量
            after_hit = uf.get_size_of_set(self.CEIL)
            
            # 填回砖块，合并
            uf.add((x,y))
            self.merge_neighbors(uf,m,n,grid,x,y)
            if x == 0:
                uf.merge((x,y),self.CEIL)
            
            # 被敲的地方和天花板连接
            if uf.is_connected((x,y),self.CEIL):
                # 敲之前和天花板连接的数量
                before_hit = uf.get_size_of_set(self.CEIL)
                res[i] = before_hit - after_hit - 1
        return res


a = Solution()
in_para1 = [[1,0,1],[1,1,1]]
in_para2 =[[0,0],[0,2],[1,1]]
resu = a.hitBricks(in_para1,in_para2)
print(resu)
