class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [str(sorted(list(string))) for string in strs]
        hmap = {}
        ans = []
        for i in range(len(sorted_strs)):
            if sorted_strs[i] not in hmap:
                hmap[sorted_strs[i]] = [strs[i]]
            else:
                hmap[sorted_strs[i]].append(strs[i])
        
        for arr in hmap.values():
            ans.append(arr)
        
        return ans