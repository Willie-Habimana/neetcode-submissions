class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1 
        l = 0 

        curr = numbers[r] + numbers[l] 

        while curr != target: 
            if curr < target:
                l += 1
            else:
                r -= 1
            curr = numbers[r] + numbers[l] 
        
        return [l+1, r+1]