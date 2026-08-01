class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ''
        for s in strs:
            ret += str(len(s))
            ret += ':'
            ret += s
        return ret

    def decode(self, s: str) -> List[str]:
        print(s)
        ret = []
        i = 0
        while i < len(s):
            length = ''
            while s[i] != ':':
                length += s[i]
                i += 1
            length = int(length)
            i += 1
            elem = ''
            while length > 0:
                elem += s[i]
                i += 1
                length -= 1
            ret.append(elem)
        
        return ret

                

