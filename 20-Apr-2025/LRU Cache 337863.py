# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.lru = OrderedDict()
        self.capacity = capacity
        
        

    def get(self, key: int) -> int:
        if  key in self.lru:
            self.lru.move_to_end(key)
            return self.lru[key]
        return -1
            
        

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru.move_to_end(key)

        self.lru[key] = value
        if len(self.lru) > self.capacity:
            self.lru.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)