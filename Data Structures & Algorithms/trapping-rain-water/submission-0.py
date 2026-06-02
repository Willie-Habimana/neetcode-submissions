class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            if height[left] < height[right]:
                ptr = left + 1
                while left < right and height[ptr] < height[left]:
                    ans += height[left] - height[ptr]
                    ptr += 1
                left = ptr
            else: 
                ptr = right - 1
                while left < right and height[ptr] < height[right]:
                    ans += height[right] - height[ptr]
                    ptr -= 1
                right = ptr
        
        return ans