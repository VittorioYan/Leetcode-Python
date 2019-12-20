from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        color = [-1]*numCourses
        route_dict = {}
        for i in range(numCourses):
            route_dict[i] = []
        for couple in prerequisites:
            route_dict[couple[0]].append(couple[1])

        def DFS(node: int) -> bool:
            if color[node] == 0:
                return False
            if color[node] == 1:
                return True
            color[node] = 0
            flag = True
            route = route_dict[node]
            for next_node in route:
                if not DFS(next_node):
                    flag = False
                    break
            color[node] = 1
            return flag

        for i in range(numCourses):
            if color[i] == 1:
                continue
            if not DFS(i):
                return False
        return True


a = Solution()
in_para1 = 1
in_para2 = []
resu = a.canFinish(in_para1, in_para2)
print(resu)
