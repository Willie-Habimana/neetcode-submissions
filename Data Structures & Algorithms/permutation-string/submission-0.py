class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_map = defaultdict(int)
        for char in s1:
            s1_map[char] += 1
        
        start = end = 0
        while end < len(s2):
            if s2[end] not in s1_map:
                while s2[end] not in s1_map and start != end:
                    s1_map[s2[start]] += 1
                    start += 1
                if start == end:
                    start += 1
                else:
                    del s1_map[s2[end]]
            else:
                s1_map[s2[end]] -= 1
                if s1_map[s2[end]] == 0:
                    del s1_map[s2[end]]
                if len(s1_map) == 0:
                    return True
            end += 1
        
        return False
            