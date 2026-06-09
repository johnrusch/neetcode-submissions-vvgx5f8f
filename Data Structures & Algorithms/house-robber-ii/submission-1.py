class Solution:
    def rob(self, nums: List[int]) -> int:
        def robbing(n_list):
            rob1, rob2 = 0, 0
            for n in n_list:
                temp = rob2
                rob2 = max(rob1 + n, rob2)
                rob1 = temp
            return rob2

        if len(nums) == 1:
            return nums[0]

        return max(robbing(nums[1:]), robbing(nums[:-1]))
            