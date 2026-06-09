class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l+r) // 2
            if nums[l] > nums[r]:
                if nums[mid] > nums[l]:
                    l = mid + 1
                elif nums[mid] == nums[l]:
                    return nums[r]
                else:
                    r = mid
            else:
                return nums[l]
        
        return nums[r]


        

        