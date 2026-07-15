class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cache = {}
        self.cost = cost

        return min(self.helper(0), self.helper(1))
    





    def helper(self, i):
        if i >= len(self.cost):
            return 0
        if i in self.cache:
            return self.cache[i]
        
        one = self.helper(i+1)
        two = self.helper(i+2)

        self.cache[i] = min(one, two) + self.cost[i]

        return self.cache[i]
        
        
        