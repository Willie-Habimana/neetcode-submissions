class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, num in enumerate(nums):
            if num not in hmap:
                hmap[target-num] = i
            else:
                return [hmap[num], i]
    
        
        