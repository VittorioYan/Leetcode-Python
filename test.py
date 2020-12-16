import random
from typing import List

def dict_update(_dict:dict,k:str,v:list):
    if k in _dict:
        _dict[k]+=v
    else:
        _dict[k]=v

def generate(length:int)->str:
    ans = []
    for _ in range(length):
        num = random.randint(1,1000)
        ans.append(num)
    return ans


    

print(generate(1000))