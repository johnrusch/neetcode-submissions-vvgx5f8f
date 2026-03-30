class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_key = {}

        for s in s1:
            s1_key[s] = s1_key.get(s, 0) + 1

        s2_key = {}

        for i in range(len(s2) - (len(s) - 1)):
            if i >= len(s1):
                s2_key[s2[i - len(s1)]] -= 1
                if s2_key[s2[i - len(s1)]] == 0:
                    del s2_key[s2[i - len(s1)]]
            s2_key[s2[i]] = s2_key.get(s2[i], 0) + 1
            if s1_key == s2_key:
                return True

        return False
            
