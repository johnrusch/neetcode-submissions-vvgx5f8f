class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for car in sorted(cars)[::-1]:
            time = (target - car[0]) / car[1]
            stack.append(time)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)