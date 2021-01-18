from typing import List
import heapq

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        size = len(stones)
        visited = [False]*size
        row,column = {},{}
        for index,stone in enumerate(stones):
            row[stone[0]] = row.get(stone[0],[])+[index]
            column[stone[1]] = column.get(stone[1],[])+[index]
        ans = 0
        def bfs(queue:set):
            if not queue:
                return
            index = queue.pop()
            cur = stones[index]
            visited[index] = True
            if cur[0] in row:
                for item in row[cur[0]]:
                    queue.add(item)
                row.pop(cur[0])
            if cur[1] in column:
                for item in column[cur[1]]:
                    queue.add(item)
                column.pop(cur[1])
            bfs(queue)

        for index,_ in enumerate(stones):
            if not visited[index]:
                ans+=1
                bfs({index})
        return size-ans
        

a = Solution()
in_para1 = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
in_para2 = 552
resu = a.removeStones(in_para1)
print(resu)
