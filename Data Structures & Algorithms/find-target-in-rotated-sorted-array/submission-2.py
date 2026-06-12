class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] > target: 
                if nums[left] > nums[mid] or nums[left] < target:
                    right = mid - 1
                elif nums[left] > target:
                    left = mid + 1
                else:
                    return left
            elif nums[mid] < target:
                if nums[right] < nums[mid] or nums[right] > target:
                    left = mid + 1
                elif nums[right] < target:
                    right = mid - 1
                else:
                    return right
            else:
                return mid
        
        return -1 



        
