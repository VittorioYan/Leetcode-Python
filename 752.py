from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def add(a):
            if a=='9':
                return '0'
            else:
                return str(int(a)+1)
        def minus(a):
            if a=='0':
                return '9'
            else:
                return str(int(a)-1)
        def find_neighbor(a:str)->list:
            neighbor = []
            for i in range(4):
                neighbor.append(a[:i]+add(a[i])+a[i+1:])
                neighbor.append(a[:i]+minus(a[i])+a[i+1:])
            return neighbor


        dp = {'0000':0}
        queue = []
        dead = set(deadends)
        if '0000' in dead:
            return -1
        queue.append('0000')
        while queue:
            cur = queue.pop(0)
            neighbor = find_neighbor(cur)
            for nei in neighbor:
                if (nei in dp and dp[cur]+1>=dp[nei]) or nei in dead:
                    continue
                else:
                    dp[nei] = dp[cur]+1
                    queue.append(nei)
            
        return dp.get(target,-1)

a = Solution()
in_para1 =["0201","0101","0102","1212","2002"]
in_para2 = '0202'
resu = a.openLock(in_para1,in_para2)
print(resu)