class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {"(":")", "{":"}","[":"]"}
        stack = []
        for paren in s:
            if paren in hmap:
                stack.append(hmap[paren])
            else:
                if stack and stack[-1] == paren:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
        