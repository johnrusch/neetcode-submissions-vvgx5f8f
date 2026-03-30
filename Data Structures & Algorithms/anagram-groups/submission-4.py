class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            seen = [0] * 26

            for c in s:
                idx = ord(c.lower()) - ord('a')
                seen[idx] += 1

            c_count = tuple(seen)

            if c_count in res:
                res[c_count].append(s)
            else:
                res[c_count] = [s]

        return list(res.values())