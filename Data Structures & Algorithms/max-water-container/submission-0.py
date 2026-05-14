class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        ans = 0
        while l < r:
            curr = min(heights[r], heights[l]) * (r-l)
            ans = max(ans, curr)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return ans
        