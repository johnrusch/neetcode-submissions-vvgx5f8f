class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry, i = True, len(digits) - 1

        while carry:
            if i >= 0:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = False
            else:
                digits.insert(0, 1)
                carry = False

            i -= 1

        return digits
