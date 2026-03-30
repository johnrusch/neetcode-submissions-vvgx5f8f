class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        s_map, t_map = {}, {}
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1

        t_match = len(t_map.keys())
        s_match = 0

        l = 0
        min_s, res = float("inf"), ""

        for r in range(len(s)):
            print('begin', s[l:r + 1])
            s_map[s[r]] = s_map.get(s[r], 0) + 1
            if s[r] in t_map:
                if s_map[s[r]] == t_map[s[r]]:
                    s_match += 1

            while s_match == t_match:
                if (r - l) + 1 < min_s:
                    min_s = (r - l) + 1
                    res = s[l:r + 1]

                s_map[s[l]] -= 1
                if s[l] in t_map:
                    if s_map[s[l]] < t_map[s[l]]:
                        s_match -= 1
                l += 1

        return res