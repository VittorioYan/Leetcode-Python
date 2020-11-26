from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        l_even = [0]
        l_odd = [0]
        ans = 0
        for index,num in enumerate(nums):
            if index%2==0:
                l_even += [l_even[-1]+num]
                l_odd += [l_odd[-1]]
            else:
                l_odd += [l_odd[-1]+num]
                l_even += [l_even[-1]]
        for index in range(len(nums)):
            if l_odd[index]+(l_even[-1]-l_even[index+1]) == l_even[index]+(l_odd[-1]-l_odd[index+1]):
                ans+=1
        return ans
        # print('l_even', l_even)
        # print('l_odd', l_odd)
        # print(ans)


a = Solution()
in_para1 = [1,2,3]
in_para2 = 552
resu = a.waysToMakeFair(in_para1)
print(resu)
