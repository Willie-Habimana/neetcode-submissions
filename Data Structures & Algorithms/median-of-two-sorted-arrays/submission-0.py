class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = 0
        l2 = 0 
        r1 = len(nums1) - 1
        r2 = len(nums2) - 1

        total = len(nums1) + len(nums2) 

        count = total - 2 if total % 2 == 0 else total - 1

        for i in range(count // 2):
            # Find lowest
            if l1 > r1:
                l2 += 1
            elif l2 > r2:
                l1 += 1
            elif nums1[l1] < nums2[l2]:
                l1 += 1
            else:
                l2 += 1

            # Find highest
            if r2 < l2:
                r1 -= 1
            elif r1 < l1:
                r2 -= 1
            elif nums2[r2] > nums1[r1]:
                r2 -= 1
            else:
                r1 -= 1
        
        if l1 > r1:
            return (nums2[r2] + nums2[l2]) / 2
        elif l2 > r2:
            return (nums1[l1] + nums1[r1]) / 2
        else: 
            return (nums1[l1] + nums2[r2]) / 2
        



