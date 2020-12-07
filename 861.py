from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        def count_column(a,column_index:int):
            answer = 0
            for index in range(len(a)):
                answer+=a[index][column_index]
            return answer

        for index in range(len(A)):
            if A[index][0]==0:
                A[index] = [abs(num-1) for num in A[index]]
        a_sum = []
        power = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]
        for i in range(len(A[0])):
            a_sum += [count_column(A,i)]
        ans= 0
        for i in range(len(a_sum)):
            ans += power[len(a_sum)-i-1]*max(a_sum[i],len(A)-a_sum[i])
        return ans

        # num_rows ,num_cloumns= len(A),len(A[0])
        # for i in range(num_rows):
        #     for j in range(1,num_cloumns):
                
# class Solution:
#     def matrixScore(self, A: List[List[int]]) -> int:

#         m=len(A)
#         n=len(A[0])
#         for i in range(m):
#             if A[i][0]==0:
#                 for j in range(n):
#                     A[i][j]=A[i][j]^1
#         r=0
#         for j in range(0,n):
#             count1=[A[i][j] for i in range(m)].count(1)     
#             r+=2**(n-j-1)*(max(count1,(m-count1)))
#         return r


a = Solution()
in_para1 = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
in_para2 = 0
resu = a.matrixScore(in_para1)
print(resu)
