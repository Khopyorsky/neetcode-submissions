class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output: list[int] = [0] * len(temperatures)
        stack = []
        for current_day, day_temperature in enumerate(temperatures):
            while stack and  day_temperature > temperatures[stack[-1]]:
                day = stack.pop()
                output[day] = current_day - day
            stack.append(current_day)
        return output