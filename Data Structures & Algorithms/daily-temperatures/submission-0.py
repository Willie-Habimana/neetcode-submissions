class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for temp in temperatures]
        stack = []

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                past_temp = stack.pop()
                days = i - past_temp[1]
                ans[past_temp[1]] = days
            stack.append((temperatures[i], i))
        
        return ans
            

        