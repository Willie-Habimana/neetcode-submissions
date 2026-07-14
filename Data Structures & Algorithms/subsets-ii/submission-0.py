class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.curr = []
        self.res = []
        self.nums = nums

        self.dfs(0)

        return self.res
    


    def dfs(self, i):
        if i == len(self.nums):
            self.res.append(self.curr.copy())
            return
        

        self.curr.append(self.nums[i])
        self.dfs(i+1)
        self.curr.pop()
        while i + 1 < len(self.nums) and self.nums[i] == self.nums[i+1]:
            i+=1
        self.dfs(i+1)

        
        
        

        