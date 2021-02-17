import random
from typing import List

def dict_update(_dict:dict,k:str,v:list):
    if k in _dict:
        _dict[k]+=v
    else:
        _dict[k]=v

def generate_str(length:int)->str:
    ans = ''
    for _ in range(length):
        num = random.randint(97,122)
        ans+=chr(num)
    return ans

def generate_list(length:int)->str:
    ans = []
    for _ in range(length):
        # num = random.randint(1,100)
        ans+=[random.randint(1,1000)]
    return ans
    

# print(generate_list(300))
# print(generate_str(300))
# print((100000-1)*(100000-2)//2%1000000007)
# print((1,2,3)>(0,1,4))
# print([2**x for x in range(32,-1,-1)])

# a = [["Bob","Bob10@m.co","Bob11@m.co","Bob1@m.co","Bob3@m.co","Bob5@m.co","Bob6@m.co","Bob7@m.co","Bob9@m.co"],["Alex","Alex10@m.co","Alex2@m.co","Alex3@m.co","Alex4@m.co","Alex6@m.co","Alex7@m.co","Alex8@m.co"],["David","David11@m.co","David2@m.co","David4@m.co","David5@m.co","David7@m.co"],["Bob","Bob12@m.co","Bob2@m.co","Bob8@m.co"],["Isa","Isa11@m.co","Isa12@m.co","Isa1@m.co","Isa2@m.co","Isa3@m.co","Isa4@m.co","Isa9@m.co"],["John","John0@m.co","John11@m.co","John12@m.co","John3@m.co","John6@m.co"],["Fern","Fern12@m.co","Fern4@m.co","Fern6@m.co","Fern9@m.co"],["Kevin","Kevin0@m.co","Kevin11@m.co","Kevin6@m.co","Kevin7@m.co","Kevin8@m.co","Kevin9@m.co"]]
# a.sort()
# print(a)

a = list(range(20))
random.shuffle(a)
print(a)