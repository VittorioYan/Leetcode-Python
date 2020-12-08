from typing import List
import bisect

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        class MyException(Exception):
            def __init__(self, *args: object,value) -> None:
                super().__init__(*args)
                self.value = value
            def __str__(self) -> str:
                return super().__str__()
        
        def dfs(history:List[int],index:int):
            if index==len(S):
                raise MyException(value=history)
            if history[-1]+history[-2]>2147483647:
                return
            target = str(history[-1]+history[-2])
            if S[index]=='0' and target!='0':
                return
            if index+len(target)<=len(S):
                if target == S[index:index+len(target)]:
                    history.append(history[-1]+history[-2])
                    dfs(history,index+len(target))
                    history.pop()

        try:
            if len(S)<3:
                return[]
            his = []

            for i in range(1,min(10,len(S)-1) if S[0]!='0'else 2):
                his.append(int(S[:i]))
                if S[i]=='0':
                    his.append(0)
                    dfs(his,i+1)
                    his.pop()
                    his.pop()
                    continue
                for j in range(1,min(10,len(S)-i)):
                    his.append(int(S[i:i+j]))
                    dfs(his,i+j)
                    his.pop()
                his.pop()
        except MyException as e:
            return e.value
        return []




a = Solution()
in_para1 = "11235813"
in_para2 = 0
resu = a.splitIntoFibonacci(in_para1)
print(resu)
