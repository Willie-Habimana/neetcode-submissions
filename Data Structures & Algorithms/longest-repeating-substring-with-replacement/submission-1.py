class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = defaultdict(int)
        l = 0
        hmap[s[l]] = 1
        max_freq = 1
        ans = 1
        for i in range(1, len(s)):
            hmap[s[i]] += 1
            max_freq = max(max_freq, hmap[s[i]])


            length = i - l + 1
            others = length - max_freq
            if others > k:
                hmap[s[l]] -= 1
                l += 1
            else:
                ans = max(ans, length)
        
        return ans


        