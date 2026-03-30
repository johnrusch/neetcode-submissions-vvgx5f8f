class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        i, res = 0, []

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            s_len = int(s[i:j])
            start = j + 1
            end = start + s_len
            res.append(s[start:end])
            i = end

        return res
