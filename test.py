from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return list(range(n))
        if n <= 2:
            return [0, 1]
        long_route = [-1] * n
        graph = [[False]*n for _ in range(n)]

        for edge in edges:
            graph[edge[0]][edge[1]] = True
            graph[edge[1]][edge[0]] = True
        graph = {}
        long_route = [-1] * n
        graph1 = {}

        for i in range(n):
            graph1[i] = []
        for edge in edges:
            graph1[edge[0]].append(edge[1])
            graph1[edge[1]].append(edge[0])
        queue = []
        for i in range(n):
            if len(graph[i]) == 1:
                long_route[i] = 0
                queue.append((i, 0))

        while queue:
            cur_point = queue.pop(0)
            c_p, depth = cur_point[0], cur_point[1]
            for next in graph1[c_p]:
                if long_route[next] == 0:
                    continue
                if long_route[next] ==-1:
                    queue.append((next, depth + 1))
                long_route[next] = depth + 1

        min_route = n + 1
        ans = []
        for i in range(n):
            if long_route[i] == 0:
                continue
            if long_route[i] < min_route:
                ans = []
                min_route = long_route[i]
            if long_route[i] == min_route:
                ans.append(i)
        return ans


a = Solution()
in_para1 = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
in_para2 = 7
resu = a.findMinHeightTrees(in_para2, in_para1)
print(resu)
