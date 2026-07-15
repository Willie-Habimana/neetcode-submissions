class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.ret = []
        self.curr = []
        self.digits = digits
        self.hmap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        self.dfs(0)

        return self.ret
    




    def dfs(self, i):
        if i == len(self.digits):
            if len(self.curr) > 0:
                self.ret.append("".join(self.curr))
            return
        
        digit = self.digits[i]
        letters = self.hmap[digit]

        for letter in letters:
            self.curr.append(letter)
            self.dfs(i+1)
            self.curr.pop()
        
        
        



        