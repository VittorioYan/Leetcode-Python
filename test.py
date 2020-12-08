import random
from typing import List

def generate(length:int)->str:
    ans = ''
    for _ in range(length):
        ans+=str(random.randint(1,10))
    return ans


    

print(generate(100))