from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(step: int, target: int, route: List[int]):
            if target > step * 9:
                return
            if step == 0 and target == 0:
                ans.append(route.copy())
                return
            if len(route) > 0:
                start = route[-1]+1
            else:
                start = 1
            for i in range(start, min(10, target+1)):
                route.append(i)
                dfs(step - 1, target - i, route)
                route.pop()

        dfs(k, n, [])
        return ans


a = Solution()
in_para1 = 3
in_para2 = 9
resu = a.combinationSum3(in_para1, in_para2)
print(resu)
