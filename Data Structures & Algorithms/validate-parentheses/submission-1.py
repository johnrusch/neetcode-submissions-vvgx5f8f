class Solution:
    def isValid(self, s: str) -> bool:
        key = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []

        for c in s:
            if c in key:
                stack.append(c)
            elif stack:
                if key[stack.pop()] != c:
                    return False
            else:
                return False

        return not stack
