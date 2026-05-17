class Solution:
    def rob(self, nums: List[int]) -> int:
        house1, house2 = 0, 0

        for num in nums:
            temp = max(num + house1, house2)
            house1 = house2
            house2 = temp
            print("temp: ", temp, " house1: ", house1, " house2: ", house2)


        return house2