class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        key = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []

        for c in s:
            if c in key:
                stack.append(c)
                continue
            if not stack or key[stack.pop()] != c:
                return False

        return not stack
