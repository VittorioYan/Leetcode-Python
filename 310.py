from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return list(range(n))
        if n <= 2:
            return [0, 1]
        graph = {}
        degree = [0] * n
        for i in range(n):
            graph[i] = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            degree[edge[0]] += 1
            degree[edge[1]] += 1
        queue = []
        dep = [-1] * n
        for i in range(n):
            if degree[i] == 1:
                queue.append((i, 0))
                dep[i] = 0

        while queue:
            current = queue.pop(0)
            c_p, depth = current[0], current[1]
            for next in graph[c_p]:
                degree[next] -= 1
                if degree[next] == 1:
                    queue.append((next, depth + 1))
                    dep[next] = depth + 1
        ans = []
        max_dep = 0
        for i in range(n):
            if dep[i] > max_dep:
                ans = []
                max_dep = dep[i]
            if dep[i] == max_dep:
                ans.append(i)

        return ans


a = Solution()
in_para1 = [[0,1],[0,2],[0,3],[3,4],[4,5]]
in_para2 = 6
resu = a.findMinHeightTrees(in_para2, in_para1)
print(resu)
