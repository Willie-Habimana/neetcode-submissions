class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]

        ret = []
        for i in range(len(nums)):
            permutations = self.permute(nums[:i] + nums[i+1:])
            for perm in permutations:
                new_perm = [nums[i]] + perm 
                ret.append(new_perm)
        
        return ret



    # def helper(self, nums):
    #     ret = []
    #     for i in range(len(nums)):
    #         permutations = self.helper(nums[:i] + nums[i+1:])
    #         for perm in permutations:
    #             ret.append(nums[i] + perm)
        
    #     return ret

        