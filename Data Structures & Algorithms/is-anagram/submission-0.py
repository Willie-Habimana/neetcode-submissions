class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = defaultdict(int)
        for char in s:
            hmap[char] += 1
        
        for char in t:
            if char not in hmap:
                return False
            hmap[char] -= 1
            if hmap[char] <= 0:
                del hmap[char]
        
        return len(hmap) == 0


        