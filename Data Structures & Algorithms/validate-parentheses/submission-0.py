class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"(": ")", "{":"}", "[":"]"}

        for char in s:
            if char not in dic:
                if len(stack) > 0 and dic[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0