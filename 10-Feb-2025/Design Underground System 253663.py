# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
       self.check_in_time = defaultdict(list)
       self.chek_out_time = defaultdict(list) 
       self.time = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_time[id].extend([stationName, t])

    def getInCheck(self) -> dict:
        return self.check_in_time
    def getOutCheck(self) -> dict:
        return self.chek_out_time

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station = self.check_in_time[id][0]
        start_time = self.check_in_time[id][1]
        self.check_in_time.pop(id)
        total_time = t - start_time
        self.time[(start_station, stationName)].append(total_time)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total = 0
        length = 0
        for time in self.time[(startStation, endStation)]:
            length += 1
            total += time
        return total / length

        


# Your UndergroundSystem object will be instantiated and called as such:
obj = UndergroundSystem()
obj.checkIn(45,"Leyton",3)
obj.checkIn(32, "Paradise", 8)
obj.checkIn(27, "Leyton", 10)
obj.checkOut(45, "Waterloo", 15)
obj.checkOut(27, "Waterloo", 20)
obj.checkOut(32, "Cambridge", 22)
print("Check IN: ", obj.getInCheck())
print("Check Out: ", obj.getOutCheck())
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)