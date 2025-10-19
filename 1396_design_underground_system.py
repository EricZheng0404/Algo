class UndergroundSystem:

    def __init__(self):
        self.users = {}
        self.trips = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # We can assume that id is not in self.users
        self.users[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkInStation, checkinTime = self.users[id]
        del self.users[id]
        twoStations = f"{checkInStation}-{stationName}"
        if twoStations in self.trips:
            currSum, currNum = self.trips[twoStations]
            self.trips[twoStations] = [currSum + (t - checkinTime), currNum + 1]
        else:
            self.trips[twoStations] = [t - checkinTime, 1] 
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        currSum, currNum = self.trips[f"{startStation}-{endStation}"]
        return currSum / currNum


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)