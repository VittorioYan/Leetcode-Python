from typing import List
from collections import OrderedDict

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        cur_tank = 0
        start_station = 0
        stat_num = len(gas)

        # def next_stat(cur_index):
        #     if cur_index == stat_num-1:
        #         return 0
        #     else:
        #         return cur_index+1
        # aim_stat = next_stat(start_station)
        # while aim_stat != start_station:
        for i in range(stat_num):
            cur_tank = cur_tank + gas[i] - cost[i]
            total_tank += gas[i] - cost[i]
            if cur_tank < 0:
                cur_tank = 0
                start_station = i+1
        if total_tank < 0:
            return -1
        return start_station


a = Solution()
gas_in = [2,3,4]
cost_in = [3,4,3]
# cost_in = [3,4,5,1,2]
# cost_in = [4,4,1,5,1]
res = a.canCompleteCircuit(gas_in, cost_in)
print(res)
