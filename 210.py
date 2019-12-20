from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        color = [0] * numCourses
        route_dict = {}
        zero_in = set(range(numCourses))
        for i in range(numCourses):
            route_dict[i] = []
        for couple in prerequisites:
            route_dict[couple[1]].append(couple[0])
            color[couple[0]] += 1
            if color[couple[0]] == 1:
                zero_in.remove(couple[0])
        route = []

        def re_color(node: int):
            for _next in route_dict[node]:
                color[_next] -= 1
                if color[_next] ==0:
                    zero_in.add(_next)
            color[node] = -1
            route.append(node)

        while len(zero_in)>0:
            pointer = zero_in.pop()
            if color[pointer] == 0:
                re_color(pointer)
        if len(route) != numCourses:
            return []
        return route


a = Solution()
in_para1 = 2
in_para2 = [[0, 1]]
resu = a.findOrder(in_para1, in_para2)
print(resu)
