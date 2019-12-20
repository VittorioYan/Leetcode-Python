from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def cal_func(poi1, poi2):
            if (poi2[0] - poi1[0]) != 0:
                k = (poi2[1] - poi1[1])/(poi2[0] - poi1[0])
                b = poi2[1] - k * poi2[0]
            else:
                k = None
                b = None

            return k, b
        max_res = 0
        poi_num = len(points)
        if poi_num < 3:
            return poi_num
        # func_k = [[0.0] * poi_num for _ in range(poi_num)]
        # func_b = [[0.0] * poi_num for _ in range(poi_num)]
        # func_dict = {}
        dp = [[False] * poi_num for _ in range(poi_num)]

        for i in range(poi_num):
            for j in range(i+1, poi_num):
                if dp[i][j]:
                    continue
                the_k, the_b = cal_func(points[i], points[j])
                dp[i][j] = True
                dp[j][i] = True
                cur_max = 0
                for l in range(poi_num):
                    if the_k is None:
                        if points[l][0] == points[i][0]:
                            dp[i][l] = True
                            dp[l][i] = True
                            dp[l][j] = True
                            dp[j][l] = True
                            cur_max += 1
                    else:
                        if points[l][0] * the_k + the_b == points[l][1]:
                            dp[i][l] = True
                            dp[l][i] = True
                            dp[l][j] = True
                            dp[j][l] = True
                            cur_max += 1
                max_res = max(max_res, cur_max)

                # if (the_k, the_b) in func_dict:
                #     func_dict[(the_k, the_b)] = func_dict[(the_k, the_b)]+1
                # else:
                #     func_dict[(the_k, the_b)] = 1
                # func_k[i][j], func_b[i][j] = cal_func(points[i], points[j])

        return max_res
        # max_res = max(func_dict.values())
        # for i in range(1, max_res*2+1):
        #     if i*(i-1) == max_res*2:
        #         return i

a = Solution()
in_para1 =[[3,1],[12,3],[3,1],[-6,-1]]
resu = a.maxPoints(in_para1)
print(resu)