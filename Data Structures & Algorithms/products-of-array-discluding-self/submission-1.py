class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)
        curr = nums[0]
        for i in range(1, len(nums)):
            ret[i] = curr 
            curr *= nums[i]
        curr = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            ret[i] *= curr
            curr *= nums[i]

        return ret   