class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        s1_dict, s2_dict = {}, {}
        for char in s:
            s1_dict[char] = s1_dict.get(char, 0) + 1
        
        for char in t:
            s2_dict[char] = s2_dict.get(char, 0) + 1

        return s1_dict == s2_dict