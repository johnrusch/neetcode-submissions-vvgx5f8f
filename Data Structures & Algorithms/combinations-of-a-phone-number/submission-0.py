class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []

        if not digits: return res
        current = []
        def backtrack(idx):
            if idx >= len(digits):
                res.append("".join(current.copy()))
                return

            for char in key_map[digits[idx]]:
                current.append(char)
                backtrack(idx + 1)
                current.pop()

        backtrack(0)
        return res