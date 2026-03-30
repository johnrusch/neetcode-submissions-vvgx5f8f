class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gram_map = {}

        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - 97] += 1

            key = tuple(chars)
            if key in gram_map:
                gram_map[key].append(s)
            else:
                gram_map[key] = [s]

        return list(gram_map.values())