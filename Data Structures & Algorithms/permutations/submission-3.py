class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # make result var
        # make backtrack function that takes list of available nums and current
        # basecase: if current == len(nums), add copy to res
        # iterate through available nums list
        # add num to current, call backtrack function taking num out of available
        # then pop num from current

        res = []

        def backtrack(num_list, current):
            if len(current) == len(nums):
                res.append(current.copy())
                return
            for i, num in enumerate(num_list):
                current.append(num)
                backtrack(num_list[:i] + num_list[i + 1:], current)
                current.pop()

        backtrack(nums, [])

        return res