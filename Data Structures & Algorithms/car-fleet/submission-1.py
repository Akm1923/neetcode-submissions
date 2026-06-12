class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = []

        for i, pos in enumerate(position):
            time = (target - pos) / speed[i]
            cars.append((pos, time))

        cars.sort(reverse=True)   # position ke according

        fleet = 0
        last_time = 0

        for pos, time in cars:

            if time > last_time:
                fleet += 1
                last_time = time

        return fleet