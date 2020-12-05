from typing import List
import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        def dict_minus_one(dic:dict,k:int):
            dic[k]-=1
            if dic[k]==0:
                del dic[k]
        task_count = collections.Counter(tasks)
        ans,aim_len,len_tasks = 0,0,len(tasks)
        while task_count:
            task_sort = sorted(task_count,key=task_count.get,reverse=True)
            for d in task_sort:
                if aim_len>n:
                    break
                if d in task_count:
                    dict_minus_one(task_count,d)
                    aim_len+=1
                    len_tasks-=1
            if len_tasks<=0:
                break
            if aim_len<=n:
                ans+=n-aim_len+1
            aim_len=0
        return ans+len(tasks)

# class Solution(object):
#     def leastInterval(self, tasks, n):
#         """
#         :type tasks: List[str]
#         :type n: int
#         :rtype: int
#         """
#         length = len(tasks)
#         if length <= 1:
#             return length
        
#         # 用于记录每个任务出现的次数
#         task_map = dict()
#         for task in tasks:
#             task_map[task] = task_map.get(task, 0) + 1
#         # 按任务出现的次数从大到小排序
#         task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        
#         # 出现最多次任务的次数
#         max_task_count = task_sort[0][1]
#         # 至少需要的最短时间
#         res = (max_task_count - 1) * (n + 1)
        
#         for sort in task_sort:
#             if sort[1] == max_task_count:
#                 res += 1
        
#         # 如果结果比任务数量少，则返回总任务数
#         return res if res >= length else length


a = Solution()
in_para1 = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
in_para2 = 5
resu = a.leastInterval(in_para1,in_para2)
print(resu)
