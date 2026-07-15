class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.curr = []
        self.n = n
        self.ans = []

        self.helper(0, 0)

        return self.ans


    def helper(self, left, right): 
        if left == right == self.n:
            self.ans.append("".join(self.curr))
            return
        

        if left < self.n:
            self.curr.append("(")
            self.helper(left + 1, right)
            self.curr.pop()
        if right < left:
            self.curr.append(")")
            self.helper(left, right + 1)
            self.curr.pop()
    