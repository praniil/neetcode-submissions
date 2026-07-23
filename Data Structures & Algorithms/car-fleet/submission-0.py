class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dict_car = {}
        stack = []
        for position, speed in zip(position, speed):
            dict_car[position] = speed

        dict_car = dict(sorted(dict_car.items(), key=lambda item: item[0], reverse=True))
        for pos, spe in dict_car.items():
            stack.append((target - pos) / spe)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
