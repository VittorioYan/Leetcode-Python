import random
from typing import List

def generate(length:int)->str:
    ans = ''
    for _ in range(length):
        num = random.randint(1,2)
        if num==1:
            ans+='R'
        else:
            ans+='D'
    return ans


    

print(generate(10000))