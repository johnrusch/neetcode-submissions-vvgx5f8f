class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # disqualify invalid input
        if len(s1) > len(s2):
            return False
            
        # create array alphabet keys for both strings
        s1_key, s2_key = [0] * 26, [0] * 26

        # fill s1 key and fill s2 key for current window
        for i in range(len(s1)):
            s1_key[ord(s1[i]) - ord("a")] += 1
            s2_key[ord(s2[i]) - ord("a")] += 1

        for i in range(len(s2) - len(s1)):
            if s1_key == s2_key:
                return True

            s2_key[ord(s2[i]) - ord("a")] -= 1
            s2_key[ord(s2[i + len(s1)]) - ord("a")] += 1

        return s1_key == s2_key
