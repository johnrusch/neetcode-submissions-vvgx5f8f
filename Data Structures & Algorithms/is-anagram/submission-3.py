class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}

        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1

        for char in t:
            if char not in hash_map:
                return False

            hash_map[char] -= 1
            if hash_map[char] == 0:
                del hash_map[char]

        return not hash_map