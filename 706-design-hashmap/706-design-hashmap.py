class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 100
        self.hm = [None for i in range(self.size)]
        
    def hashfunc(self, num):
        return num%self.size
    
    def print_li(self, itr):
        while itr:
            print(itr.key, itr.value)
            itr = itr.next
        return

    def put(self, key: int, value: int) -> None:
        index = self.hashfunc(key)
        node = Node(key, value)
        if not self.hm[index]:
            self.hm[index] = node
        else:
            itr = self.hm[index]
            prev = None
            while itr:
                if itr.key == key:
                    itr.value = value
                    return
                prev = itr
                itr = itr.next
            prev.next = node
    
    def get(self, key: int) -> int:
        index = self.hashfunc(key)
        itr = self.hm[index]
        if itr!=None:
            while itr:
                if itr.key == key:
                    return itr.value
                itr = itr.next
        return -1

    def remove(self, key: int) -> None:
        index = self.hashfunc(key)
        itr = self.hm[index]
        if itr == None:
            return
        prev = None
        while itr:
            if itr.key == key:
                if prev == None:
                    self.hm[index] = itr.next
                else:
                    prev.next = itr.next
                return
            prev = itr
            itr = itr.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)