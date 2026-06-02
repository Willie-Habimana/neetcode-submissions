class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        left = 0
        freq_map = defaultdict(int)
        freq_map[s[left]] = 1
        max_freq = 1
        ans = 1
        for right in range(1, len(s)):
            # Update freq map and max freq
            freq_map[s[right]] += 1
            max_freq = max(max_freq, freq_map[s[right]])

            # Check if window is valid
            window_length = right - left + 1
            others = window_length - max_freq
            if others > k:
                freq_map[s[left]] -= 1
                left += 1
            
            ans = right - left + 1

        
        return ans