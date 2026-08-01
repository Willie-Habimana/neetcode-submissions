class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        ans = []
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                summ = nums[j] + nums[k]
                if summ < target:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif summ > target:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i-1]:
                i +=1
        return ans




        