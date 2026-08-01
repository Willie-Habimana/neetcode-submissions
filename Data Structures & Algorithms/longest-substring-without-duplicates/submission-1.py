class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l = 0
        r = 1
        seen = set()
        seen.add(s[l])
        ans = 1
        while r < len(s):
            if s[r] in seen: 
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            else:
                seen.add(s[r])
                ans = max(ans, r - l + 1)
            r += 1
        return ans




        