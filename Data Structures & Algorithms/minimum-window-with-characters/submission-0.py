class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        ans = None
        char_map = defaultdict(int)
        for char in t:
            char_map[char] += 1
        seen_count = 0
        start = 0
        while start < len(s) and s[start] not in char_map:
            start += 1 
        end = start
        while end < len(s):
            if s[end] in char_map:
                char_map[s[end]] -= 1
                if char_map[s[end]] == 0:
                    seen_count += 1
                    if seen_count == len(char_map):
                        if ans == None or len(ans) > end - start + 1:
                            ans = s[start:end+1]
                        while seen_count == len(char_map):
                            while s[start] not in char_map:
                                start += 1
                            if s[start] in char_map:
                                char_map[s[start]] += 1
                                if char_map[s[start]] > 0:
                                    if ans == None or len(ans) > end - start + 1:
                                        ans = s[start:end+1]
                                    seen_count -= 1
                            start += 1
                        while start < len(s) and s[start] not in char_map:
                                start += 1
            end += 1    

        return "" if ans == None else ans