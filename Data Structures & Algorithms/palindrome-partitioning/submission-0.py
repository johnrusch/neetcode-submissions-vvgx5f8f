class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s1):
            return s1 == s1[::-1]

        res = []
        current = []
        def backtrack(start):
            if start >= len(s):
                res.append(current.copy())
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if isPalindrome(substring):
                    current.append(substring)
                    backtrack(end)
                    current.pop()

        backtrack(0)
        return res