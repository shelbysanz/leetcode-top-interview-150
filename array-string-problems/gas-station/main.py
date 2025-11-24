class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tank = 0
        starting_index = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                starting_index = i + 1
                tank = 0
        return starting_index
