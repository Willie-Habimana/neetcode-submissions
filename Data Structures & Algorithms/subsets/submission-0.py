class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        
        subsets = self.subsets(nums[1:])

        new_subsets = []
        for subset in subsets:
            new_subsets.append([nums[0]] + subset)

        return subsets + new_subsets