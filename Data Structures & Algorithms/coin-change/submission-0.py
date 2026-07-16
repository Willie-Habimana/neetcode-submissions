class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        self.coins = coins
        self.cache = {}

        return self.dp(0, amount)

    def dp(self, i, amount):
        if i == len(self.coins):
            return -1
        if self.coins[i] > amount:
            return -1
        if amount - self.coins[i] == 0:
            return 1
        
        if (i, amount) in self.cache:
            return self.cache[(i, amount)]
        

        take = self.dp(i, amount - self.coins[i])
        leave = self.dp(i+1, amount)

        if take == -1 and leave == -1:
            self.cache[(i, amount)] = -1
            return -1
        
        if take == -1:
            self.cache[(i, amount)] = leave
            return leave
        
        if leave == -1:
            self.cache[(i, amount)] = take + 1
            return take + 1
        
        self.cache[(i, amount)] = min(take + 1, leave)
        return self.cache[(i, amount)]