from typing import List

class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace('-','')
        number = number.replace(' ','')
        ans = ''
        couple = int(len(number)/3)*3
        for i in range(couple):
            ans+=number[i]
            if i%3 == 2:
                ans+='-'
        if len(number)-couple==2:
            ans +=number[-2:]
        elif len(number)-couple==1:
            ans = ans[:-4]+number[-4:-2]+'-'+number[-2:]
        else:
            ans = ans[:-1]
        return ans


a = Solution()
in_para1 = "12"
in_para2 = "execution"
resu = a.reformatNumber(in_para1)
print(resu)
