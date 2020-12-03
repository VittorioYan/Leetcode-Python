from typing import List

# 虽然理论上线性的欧拉筛但是因为取余太慢导致并没有埃式快
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         prime = []
#         all_num = [0]*n
#         for i in range(2,n):
#             if not all_num[i]:
#                 prime.append(i)
#             for j in range(len(prime)):
#                 k = i*prime[j]
#                 if k>=n:
#                     break
#                 all_num[k]=1
#                 if i%prime[j]==0:
#                     break
#         return len(prime)

class Solution:
    def countPrimes(self, n: int) -> int:
        all_num = [1]*n
        all_num[0] = all_num[1] = 0
        for i in range(2,int(n**0.5)+1):
            if all_num[i]:
                # 这个切片太帅了 from powcai
                all_num[i*i:n:i] = [0]*len(all_num[i * i: n: i])
        return sum(all_num)
        

a = Solution()
in_para1 = 10
in_para2 = 10
resu = a.countPrimes(in_para1)
print(resu)
