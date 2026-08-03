class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = nums[0]
        currMax = nums[0]
        prod = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            prods = [nums[i], nums[i] * currMax, nums[i] * currMin]
            currMax = max(prods)
            currMin = min(prods)
            res = max(res, currMax)
        
        return res
        