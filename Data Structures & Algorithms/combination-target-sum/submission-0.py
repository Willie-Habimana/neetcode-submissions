class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.curr = []
        self.nums = nums

        self.depthFirstSearch(0, target)

        return self.res



    

    def depthFirstSearch(self, i, target):
        if target == 0:
            self.res.append(self.curr.copy())
            return
        elif target < 0:
            return
        elif i == len(self.nums):
            return
        
        self.curr.append(self.nums[i])
        self.depthFirstSearch(i, target-self.nums[i])
        self.curr.pop()
        self.depthFirstSearch(i+1, target)
        
        
        


        