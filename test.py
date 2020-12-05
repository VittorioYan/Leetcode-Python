import random
from typing import List

def generate(length:int)->List:
    shuzu = []
    for _ in range(length):
        shuzu.append(str(chr(random.randint(ord('A'),ord('Z')))))
    return '[\"'+'\",\"'.join(shuzu)+'\"]'

print(generate(3600))