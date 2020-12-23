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
        ans+=[[random.randint(1,100),random.randint(1,100),random.randint(1,100)]]
    return ans
    

print(generate_str(1000))
# print((1,2,3)>(0,1,4))
