class Solution:
    delimiter = '#'

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + Solution.delimiter + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != Solution.delimiter:
                j += 1
            sl = int(s[i:j])
            i = j + 1
            j = i + sl
            res.append(s[i:j])
            i = j

        return res