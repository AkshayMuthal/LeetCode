class Solution(object):
    def curr_station(self, ind, stops, distance, fuel, stations, target):
        if fuel<0:
            return
        
        if distance + fuel >= target:
            self.min_stops = min(self.min_stops, stops)
            return
        
        if ind+1<len(stations):
            diff = stations[ind+1][0]-distance
        else:
            diff = target - distance
        
        self.curr_station(ind+1, stops, distance+diff, fuel-diff, stations, target)
        if ind>=0:
            self.curr_station(ind+1, stops+1, distance+diff, fuel-diff+stations[ind][1], stations, target)
    
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in xrange(i, -1, -1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)

        for i, d in enumerate(dp):
            if d >= target: return i
        return -1