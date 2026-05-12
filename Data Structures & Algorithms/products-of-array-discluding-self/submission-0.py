class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for num in nums]
        prod = nums[0]
        for i in range(1, len(nums)):
            ans[i] = prod
            prod *= nums[i]

        prod = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            ans[i] *= prod
            prod *= nums[i]
        
        return ans