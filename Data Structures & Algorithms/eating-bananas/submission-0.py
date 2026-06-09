class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(speed):
            return sum(math.ceil(pile/speed) for pile in piles) <= h
        
        l = 1
        r = max(piles)

        while l < r:
            mid = (l+r) // 2
            if possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
        