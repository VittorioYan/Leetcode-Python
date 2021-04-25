from typing import List, Sequence
import collections
import bisect

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        cur_water = 0
        cur_pos,cur_height = 0,0
        for index,hei in enumerate(height):
            if hei>=cur_height:
                ans+=cur_water
                cur_water = 0
                cur_pos = index
                cur_height = hei
            else:
                cur_water+=cur_height-hei
        cur_water = 0
        cur_height = 0
        for i in range(len(height)-1,cur_pos-1,-1):
            hei = height[i]
            if hei>=cur_height:
                ans+=cur_water
                cur_water = 0
                cur_height = hei
            else:
                cur_water+=cur_height-hei
        return ans

a = Solution()
in_para1 = [6, 16, 10, 17, 16, 14, 14, 0, 12, 1, 9, 3, 17, 5, 9]
in_para2 = 4
resu = a.trap(in_para1)
print(resu)
