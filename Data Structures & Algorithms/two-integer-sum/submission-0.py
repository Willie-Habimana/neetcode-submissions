class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in hmap:
                hmap[target-num] = i
            else:
                return [hmap[num], i]
        
        return [None, None]
        