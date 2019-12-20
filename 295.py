from typing import List
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, -num)
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        if len(self.max_heap) - len(self.min_heap) >= 2:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap[0] - self.min_heap[0]) / 2
        else:
            return self.max_heap[0]


a = MedianFinder()
a.addNum(-1)
a.addNum(-2)
a.addNum(-1)
a.addNum(-3)
a.addNum(3)
a.addNum(1)
a.addNum(2)
a.addNum(1)
a.addNum(3)
a.addNum(3)
print(a.findMedian())
