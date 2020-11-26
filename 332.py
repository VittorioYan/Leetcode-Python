from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        route = {}
        itinerary = []
        next_num = {}
        aim_len = len(tickets) + 1

        for ticket in tickets:
            from_place = ticket[0]
            to_place = ticket[1]
            if from_place in route:
                route[from_place].append(to_place)
            else:
                route[from_place] = [to_place]
        for fp in route.keys():
            route[fp].sort(reverse=True)
            next_num[fp] = [0]*(len(route[fp])+1)
            next_num[fp][-1] = len(route[fp])

        cur_place = 'JFK'

        def go_next(cur_p: str):
            itinerary.append(cur_p)
            if len(itinerary) == aim_len:
                raise RuntimeError('testError')
            if cur_p not in route or next_num[cur_p][-1] == 0:
                itinerary.pop()
                return
            for i in range(len(next_num[cur_p]) - 2, -1, -1):
                if next_num[cur_p][i] == 1:
                    continue
                next_num[cur_p][-1] -= 1
                next_num[cur_p][i] = 1
                go_next(route[cur_p][i])
                next_num[cur_p][-1] += 1
                next_num[cur_p][i] = 0
            itinerary.pop()

        try:
            go_next(cur_place)
        except RuntimeError:
            return itinerary


a = Solution()
in_para1 = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
# in_para1 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
in_para2 = 9
resu = a.findItinerary(in_para1)
print(resu)
