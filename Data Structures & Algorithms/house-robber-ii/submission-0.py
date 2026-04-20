class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(nlist):
            rob1, rob2 = 0, 0
            for n in nlist:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        if len(nums) == 1:
            return nums[0]

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))