class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, tar, curr):
            if i >= len(nums):
                return

            if tar < 0:
                return
            if tar == 0:
                ans.append(curr)
                return
            
            # Take
            dfs(i, tar-nums[i], curr + [nums[i]])
            # Leave
            dfs(i+1, tar, curr)
            
            
        dfs(0, target, [])
        return ans


        
        
        


        