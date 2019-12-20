from typing import List


class SegaTree:
    def __init__(self, l, r, val):
        self.l = l
        self.r = r
        self.val = val
        self.l_node = None
        self.r_node = None
        if l < r:
            mid = (r + l) >> 1
            self.l_node = SegaTree(l, mid, val)
            self.r_node = SegaTree(mid + 1, r, val)

    def change_val(self, l, r, val):
        if self.r < l:
            return
        if self.l > r:
            return
        if (l == self.l and r >= self.r) or (l <= self.l and r == self.r) or (l < self.l and r > self.r):
            self.val = max(self.val, val)
            return
        self.l_node.change_val(l, r, val)
        self.r_node.change_val(l, r, val)

    def query(self, poi, max_val):
        if self.l == self.r == poi:
            return max(max_val, self.val)
        if poi <= (self.l + self.r) >> 1:
            return self.l_node.query(poi, max(max_val, self.val))
        else:
            return self.r_node.query(poi, max(max_val, self.val))


class Solution:
    def getSkyline1(self, buildings: List[List[int]]) -> List[List[int]]:
        import bisect
        res = [[0, 0]]
        # 记录 [left, height], [right, height]
        loc = []
        for l, r, h in buildings:
            # 为了排序让 left那边靠前, 所以让高度取负
            loc.append([l, -h])
            loc.append([r, h])
        loc.sort()
        heap = [0]

        for x, h in loc:
            if h < 0:
                bisect.insort(heap, h)
            else:
                heap.remove(-h)
            cur = -heap[0]
            if res[-1][1] != cur:
                res.append([x, cur])

        return res[1:]

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if len(buildings) == 0:
            return buildings
        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

        right_end = 0
        for building in buildings:
            right_end = max(right_end, building[1])
        if right_end > 10000:
            return self.getSkyline1(buildings)
        sega_tree = SegaTree(0, right_end + 2, 0)
        for building in buildings:
            sega_tree.change_val(building[0], building[1], building[2])
        res = []
        last = 0
        for i in range(right_end + 2):
            cur = sega_tree.query(i, 0)
            if cur > last:
                last = cur
                res.append([i, cur])
            if cur < last:
                last = cur
                res.append([i - 1, cur])
        return res


a = Solution()
in_para1 = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
in_para2 = 9
resu = a.getSkyline1(in_para1)
print(resu)
