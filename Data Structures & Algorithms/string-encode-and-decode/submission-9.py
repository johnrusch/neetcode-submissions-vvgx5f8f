class Solution:

    def __init__(self):
        self.dl = '#'

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f"{len(s)}{self.dl}{s}"

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # get length of string
            j = i
            while s[j] != self.dl:
                j += 1
            curr_len = int(s[i:j])

            # add string to res list
            c1 = j + 1
            res.append(s[c1:c1 + curr_len])

            # update i to index after current string
            i = c1 + curr_len
        return res
