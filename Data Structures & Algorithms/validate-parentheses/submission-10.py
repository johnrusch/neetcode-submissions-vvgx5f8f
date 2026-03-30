class Solution:
    def isValid(self, s: str) -> bool:
        char_key = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []

        for c in s:
            if c in char_key:
                stack.append(c)
            elif stack:
                top = stack.pop()
                if char_key[top] != c:
                    return False
            else:
                return False

        return not stack