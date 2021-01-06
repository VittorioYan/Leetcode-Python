from typing import List, Sequence
import collections
import bisect
import itertools
def func(m,n):
        a=b=result=1
        if m<n:
            print("n不能小于m 且均为整数")
        elif ((type(m)!=int)or(type(n)!=int)):
            print("n不能小于m 且均为整数")
        else:
            minNI=min(n,m-n)#使运算最简便
            for j in range(0,minNI):
            #使用变量a,b 让所用的分母相乘后除以所有的分子
                a=a*(m-j)
                b=b*(minNI-j)
                result=a//b #在此使用“/”和“//”均可，因为a除以b为整数
            return result   
class Solution:
    
    def countPairs(self, deliciousness: List[int]) -> int:
        ready = collections.Counter(deliciousness)
        square = [2**x for x in range(23)]
        flag = {}
        ans = 0
        for key,val in ready.items():
            for i in range(22,-1,-1):
                cur = square[i]-key
                if cur<key:
                    break
                if cur==key and (key,cur) not in flag:
                    ans+= val*(val-1)//2
                    if ans>(1000000007):ans-=1000000007
                    flag[(key,cur)] = True
                    continue
                if cur in ready and (key,cur) not in flag:
                    ans+=val*ready[square[i]-key]
                    if ans>(1000000007):ans-=1000000007
                    flag[(key,cur)] = True
            
        return ans%(1000000007)



a = Solution()
in_para1 = [1,3,5,7,9]
in_para2 = "execution"
resu = a.countPairs(in_para1)
print(resu)
