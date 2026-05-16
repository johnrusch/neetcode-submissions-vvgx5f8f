class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        seen = [0] * 26

        for c in s:
            seen[ord(c) - ord('a')] += 1

        for c in t:
            seen[ord(c) - ord('a')] -= 1

        return seen == [0] * 26

        
