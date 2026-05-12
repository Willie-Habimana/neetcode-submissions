class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ret = ""
        for s in strs:
            for char in s:
                if char != "|" and char != "/":
                    ret += char
                elif char == "/":
                    ret += "//"
                else:
                    ret += "/"
                    ret += char
            ret += "|"
        return ret

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        l = []
        i = 0
        curr = ""
        while i < len(s):
            if s[i] != "|" and s[i] != "/":
                curr += s[i]
            elif s[i] == "|":
                l.append(curr)
                curr = ""
            elif i + 1 < len(s) and (s[i+1] == "|" or s[i+1] == "/"):
                curr += s[i+1]
                i += 1
            else:
                curr += "/"
            i += 1
        return l
            
                

            

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))