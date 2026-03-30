class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            cs = numbers[i] + numbers[j]
            if target > cs:
                i += 1
            elif target < cs:
                j -= 1
            else:
                return [i + 1, j + 1]

        return [-1]