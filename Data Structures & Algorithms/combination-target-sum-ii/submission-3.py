class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.curr = []
        self.candidates = candidates
        self.candidates.sort()

        self.depthFirstSearch(0, target)

        return self.res

    def depthFirstSearch(self, i, target):
        if target == 0:
            self.res.append(self.curr.copy())
            return
        elif i == len(self.candidates) or target < 0:
            return
        
        num = self.candidates[i]
        self.curr.append(num)
        self.depthFirstSearch(i+1, target-num)
        self.curr.pop()
        while i + 1 < len(self.candidates) and self.candidates[i] == self.candidates[i+1]:
            i += 1
        self.depthFirstSearch(i+1, target)
        