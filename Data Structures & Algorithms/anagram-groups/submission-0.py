class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        ans = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in hmap:
                ans.append([word])
                hmap[sorted_word] = len(ans) - 1
            else:
                ans[hmap[sorted_word]].append(word)
        
        return ans