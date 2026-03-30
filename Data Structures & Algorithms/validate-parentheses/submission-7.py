class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        key = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        for c in s:
            if c in key:
                stack.append(c)
            else:
                if not stack or key[stack.pop()] != c:
                    return False

        return not stack

