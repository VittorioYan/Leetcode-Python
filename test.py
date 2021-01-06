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
print((100000-1)*(100000-2)//2%1000000007)
# print((1,2,3)>(0,1,4))
# print([2**x for x in range(32,-1,-1)])