class Solution:
    def numDecodings(self, s: str) -> int:
        # bottom up solution
        dp1, dp2 = 1, 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                curr = 0
            else:
                curr = dp1

            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                curr += dp2

            tmp = dp1
            dp1 = curr
            dp2 = tmp

        return dp1