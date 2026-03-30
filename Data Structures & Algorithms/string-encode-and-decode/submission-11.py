class Solution:

    def __init__(self):
        self.dl = '#'

    def encode(self, strs: List[str]) -> str:
        enc = ''
        for s in strs:
            enc += f"{len(s)}{self.dl}{s}"

        return enc

    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != self.dl:
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            dec.append(s[i:j])
            i = j

        return dec
