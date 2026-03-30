class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l, res, maxf = 0, 0, 0

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            maxf = max(maxf, counts[s[r]])
            if (r - l + 1) - maxf > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res