from typing import List, Sequence
import collections
import bisect

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        ans = 0
        size = len(nums)
        pre,last = [0]*(size+1),[0]*(size+1)
        for i in range(1,size+1):
            pre[i] = pre[i-1]+nums[i-1]
            last[i] = last[i-1]+nums[size-i]
        if pre[-1] ==0:
            return ((size-1)*(size-2)//2)%1000000007
        for i in range(1,size+1):
            aim = (pre[-1]-pre[i])/2
            index_right = size-bisect.bisect_left(last,aim)
            if index_right ==-1:
                    index_right = size-1
            if pre[i]==0:
                index_left = i+1
            else:
                index_left = bisect.bisect_left(pre,2*pre[i])
            if index_right>=index_left:
                ans += index_right-index_left+1
                if ans>=1000000007:
                    ans-=1000000007
        return ans%(1000000007)
        
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        ans = 0
        
        size = len(nums)
        flag = [[False]*(size+1) for _ in range(size+1)]
        pre = [0]*(size+1)
        for i in range(1,size+1):
            pre[i] = pre[i-1]+nums[i-1]
        def find(left,right):
            nonlocal ans
            if left==right or flag[left][right]:
                return
            flag[left][right] = True
            if pre[left]<=pre[right]-pre[left]<=pre[-1]-pre[right]:
                ans+=1
                # print(left,right)
            find(left+1,right)
            find(left,right-1)
        find(1,size-1)
        return ans%(1000000007)

a = Solution()
in_para1 = [0,3,3]
in_para2 = "execution"
resu = a.waysToSplit(in_para1)
print(resu)
