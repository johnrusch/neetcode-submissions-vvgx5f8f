# THE TRICK IS THAT YOU CAN USE A TUPLE AS A KEY IN A DICTIONARY,
# BUT YOU CAN'T USE A LIST AS A KEY IN A DICTIONARY

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        
        return res.values()