class UndergroundSystem:

    def __init__(self):
        self.cust_station = {}
        self.route_map = defaultdict(int)
        self.route_time = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cust_station[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in = self.cust_station.pop(id)
        
        self.route_map[(check_in[0], stationName)] += t - check_in[1] 
        self.route_time[(check_in[0], stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return float(self.route_map[route]/self.route_time[route])

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation) 