class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        schedule = []
        for numPeople, from_, to_ in trips:
            schedule.append((from_, numPeople))
            schedule.append((to_, -numPeople))
        schedule.sort(key=lambda x: (x[0], x[1]))
        currPassenger = 0
        for _, delta in schedule:
            currPassenger += delta
            if currPassenger > capacity:
                return False
        return True
