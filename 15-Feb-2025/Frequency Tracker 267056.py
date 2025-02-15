# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

from collections import defaultdict 
class FrequencyTracker:
    def __init__(self):
        self.values = defaultdict(int)
        self.freq = defaultdict(int)


    def add(self, number: int) -> None:
            prev = self.values[number]
            self.values[number] += 1
            self.freq[prev] -= 1
            self.freq[prev + 1] += 1

    def deleteOne(self, number: int) -> None:
        prev = self.values[number]
        if prev == 0:
            return 
        self.values[number] -= 1
        self.freq[prev] -= 1
        self.freq[prev - 1] += 1
        
    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] >= 1 
        


# Your valuesuencyTracker object will be instantiated and called as such:
# obj = valuesuencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasvaluesuency(valuesuency)