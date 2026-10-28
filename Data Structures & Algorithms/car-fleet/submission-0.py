class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        cars = sorted(zip(positions, speeds), reverse=True)
        fleets: list[float] = []
        for car in cars:
            position, speed = car
            time_to_finish = (target - position) / speed
            if not fleets or time_to_finish > fleets[-1]:
                fleets.append(time_to_finish)

        return len(fleets)
