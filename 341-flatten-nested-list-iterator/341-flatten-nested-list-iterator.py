# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.l = []
        self.ind = 0
        for i in range(len(nestedList)):
            self.add_to_list(nestedList[i])
        self.len = len(self.l)
    
    def add_to_list(self, nested_list):
        if nested_list.isInteger():
            self.l.append(nested_list.getInteger())
        else:
            ls = nested_list.getList()
            for i in ls:
                self.add_to_list(i)
    
    def next(self) -> int:
        if self.ind<self.len:
            val = self.l[self.ind]
            self.ind+=1
            return val
    
    def hasNext(self) -> bool:
        if self.ind<self.len:
            return True
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())














