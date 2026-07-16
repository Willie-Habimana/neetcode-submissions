class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s[0]]]
        self.ans = []
        self.curr = []
        self.s = s

        self.helper(0)

        return self.ans


    def helper(self, i):
        if i >= len(self.s):
            self.ans.append(self.curr.copy())
            return
        start = i
        end = start + 1
        while end <= len(self.s):
            if self.s[start:end] == self.s[start:end][::-1]:
                self.curr.append(self.s[start:end])
                self.helper(end)
                self.curr.pop()
            end += 1
        





        