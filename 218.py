from typing import List
import heapq

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

class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # 对于一个 building, 他由 (l, r, h) 三元组组成, 我们可以将其分解为两种事件: 
        #     1. 在 left position, 高度从 0 增加到 h(并且这个高度将持续到 right position); 
        #     2. 在 right position, 高度从 h 降低到 0. 
        # 由此引出了 event 的结构: 在某一个 position p, 它引入了一个高度为 h 的 skyline, 将一直持续到另一 end postion
        
        # 对于在 right position 高度降为 0 的 event, 它的持续长度时无效的
        # 只保留一个 right position event, 就可以同时触发不同的两个 building 在同一 right position 从各自的 h 降为 0 的 event, 所以对 right position events 做集合操作会减少计算量
        
        # 由于需要从左到右触发 event, 所以按 postion 对 events 进行排序
        # 并且, 对于同一 positon, 我们需要先触发更高 h 的事件, 先触发更高 h 的事件后, 那么高的 h 相比于低的 h 会占据更高的 skyline, 低 h 的 `key point` 就一定不会产生; 相反, 可能会从低到高连续产生冗余的 `key point`
        # 所以, event 不仅需要按第一个元素 position 排序, 在 position 相同时, 第二个元素 h 也是必须有序的
        events = sorted([(l, -h, r) for l, r, h in buildings] + list({(r, 0, 0) for l, r, h in buildings}))
        
        # res 记录了 `key point` 的结果: [x, h]
        # 同时 res[-1] 处的 `key point` 代表了在下一个 event 触发之前, 一直保持的最高的 skyline
        
        # hp 记录了对于一条高为 h 的 skyline, 他将持续到什么 position 才结束: [h, endposition]
        # 在同时有多条 skyline 的时候, h 最高的那条 skyline 会掩盖 h 低的 skyline, 因此在 event 触发时, 需要得到当前最高的 skyline
        # 所以利用 heap 结构存储 hp, 它的第一个值永远为列表中的最小值: 因此在 event 中记录的是 -h, heap 结构就会返回最高的 skyline. 同时, h 必须在 endposition 之前, 因为它按第一个元素排序
        res, hp = [[0, 0]], [(0, float('inf'))]

        for l, neg_h, r in events:
            # 触发 event 时, 首先要做的就是清除已经到 endposition 的 skyline
            # hp: [h, endposition]
            # 如果当前 position 大于等于了 hp 中的 endposition, 那么该 skyline 会被清除掉
            # 由于在有 high skyline 的情况下, low skyline 不会有影响, 因此, 只需要按从高到低的方式清除 skyline, 直到剩下一个最高的 skyline 并且它的 endposition 大于当前 position
            while l >= hp[0][1]: 
                heapq.heappop(hp)
            
            # 对于高度增加到 h 的时间(neg_h < 0), 我们需要添加一个 skyline, 他将持续到 r 即 endposition
            if neg_h:
                heapq.heappush(hp, (neg_h, r))
            
            # 由于 res[-1][1] 记录了在当前事件触发之前一直保持的 skyline
            # 如果当前事件触发后 skyline 发生了改变
            #     1. 来了一条新的高度大于 h 的 skyline
            #     2. res[-1] 中记录的 skyline 到达了 endposition
            # 这两种事件都会导致刚才持续的 skyline 与现在最高的 skyline 不同; 同时, `key point` 产生了, 他将被记录在 res 中 
            if res[-1][1] != -hp[0][0]:
                res.append([l, -hp[0][0]])
        
        return res[1:]

a = Solution()
in_para1 = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
in_para2 = 9
resu = a.getSkyline1(in_para1)
print(resu)
