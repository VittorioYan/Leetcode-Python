from typing import List

# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         qd = collections.deque([i for i, s in enumerate(senate) if s == "D"])
#         qr = collections.deque([i for i, s in enumerate(senate) if s == "R"])

#         while qr and qd:
#             if qr[0] < qd[0]:
#                 qd.popleft()
#                 qr.append(qr.popleft() + len(senate))
#             else:
#                 qr.popleft()
#                 qd.append(qd.popleft() + len(senate))
#         return "Dire" if not qr else "Radiant"


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        def handle_str(in_senta:str)->str:
            count_r,count_d,right_r,right_d= 0,0,0,0
            new_senta = ''
            for turn in list(in_senta):
                if turn=='R':
                    if right_d>0:
                        right_d-=1
                    else:
                        new_senta+='R'
                        count_r+=1
                        right_r+=1
                if turn=='D':
                    if right_r>0:
                        right_r-=1
                    else:
                        new_senta+='D'
                        count_d+=1
                        right_d+=1
            if count_r-right_d<=0:
                return 'Dire'
            if count_d-right_r<=0:
                return 'Radiant'
            new_new_senta = ''
            for cha in new_senta:
                if cha=='R':
                    if right_d>0:
                        right_d-=1
                    else:
                        new_new_senta+='R'
                if cha=='D':
                    if right_r>0:
                        right_r-=1
                    else:
                        new_new_senta+='D'
            return handle_str(new_new_senta)
                
        return handle_str(senate)


a = Solution()
in_para1 = "DDRRR"
in_para2 = 5
resu = a.predictPartyVictory(in_para1)
print(resu)
