class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hmap = {}
        for num in nums:
            if num not in hmap:
                hmap[num] = [None, None]
                if num-1 in hmap:
                    hmap[num-1][1] = num
                    hmap[num][0] = num - 1
                if num+1 in hmap:
                    hmap[num+1][0] = num
                    hmap[num][1] = num + 1
        
        ans = 0
        seen = set()
        for num in nums:
            if num in seen:
                continue
            count = 0
            stack = [num]
            while stack:
                curr = stack.pop()
                seen.add(curr)
                if hmap[curr][0] != None and hmap[curr][0] not in seen:
                    stack.append(hmap[curr][0])
                if hmap[curr][1] != None and hmap[curr][1] not in seen:
                    stack.append(hmap[curr][1])
                count += 1
            ans = max(ans, count)

                

        
        return ans 
                





            
            
              