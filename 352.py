from typing import List
from sortedcontainers import SortedList
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sl = SortedList([])

    def addNum(self, val: int) -> None:
        self.sl.add(val)

    def getIntervals(self) -> List[List[int]]:
        ans = []
        l,last = self.sl[0],self.sl[0]
        for item in self.sl[1:]:
            if item==last+1:
                last = item
                continue
            elif item==last:
                continue
            else:
                ans.append([l,last])
                l = last = item
        ans.append([l,last])
        return ans

obj = SummaryRanges()
obj.addNum(1)
param_2 = obj.getIntervals()
print(param_2)
obj.addNum(3)
param_2 = obj.getIntervals()
print(param_2)
obj.addNum(7)
param_2 = obj.getIntervals()
print(param_2)
obj.addNum(2)
param_2 = obj.getIntervals()
print(param_2)
obj.addNum(6)
param_2 = obj.getIntervals()
print(param_2)

