class Solution:
    def isValid(self, s: str) -> bool:
        parens = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = deque()

        for c in s:
            if c in parens:
                stack.append(c)
            else:
                if not stack or parens[stack.pop()] != c:
                    return False

        return not stack
