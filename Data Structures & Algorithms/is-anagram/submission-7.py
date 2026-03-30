class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_key, t_key = {}, {}

        for c in s:
            if c in s_key:
                s_key[c] += 1
            else:
                s_key[c] = 1

        for c in t:
            if c in t_key:
                t_key[c] += 1
            else:
                t_key[c] = 1

        return s_key == t_key
