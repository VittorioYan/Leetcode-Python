from typing import List
import itertools

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.lis = []
        while iterator.hasNext():
            self.lis.append(iterator.next())

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.lis[0]

    def next(self):
        """
        :rtype: int
        """
        u = self.lis.pop(0)
        return u

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.lis)


# Your PeekingIterator object will be instantiated and called as such:
nums = [1,2,3]
iter = PeekingIterator(Iterator(nums))
while iter.hasNext():
    val = iter.peek()   # Get the next element but not advance the iterator.
    iter.next()         # Should return the same value as [val].
