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
        self.stack = nestedList[::-1]    
    
    def prepare_stack(self, li):
        for i in range(len(li)-1, -1, -1):
            self.stack.append(li[i])
    
    def next(self) -> int:
        return self.stack.pop()
    
    def hasNext(self) -> bool:
        while len(self.stack)>0 and self.stack[-1].getInteger()==None:
            li = self.stack.pop().getList()
            self.prepare_stack(li)
        
        if len(self.stack)>0:
            return True
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())














