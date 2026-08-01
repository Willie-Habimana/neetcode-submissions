class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        count = Counter(t)
        seen = set()
        ans = ""
        l = 0
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    seen.add(s[i])

                while len(seen) == len(count):
                    if ans == '' or len(ans) > i - l + 1:
                        ans = s[l:i+1]
                    if s[l] in count:
                        count[s[l]] += 1
                        if count[s[l]] > 0:
                            seen.remove(s[l])
                    l += 1
                while l < len(s) and s[l] not in count:
                    l += 1
        
        return ans



        