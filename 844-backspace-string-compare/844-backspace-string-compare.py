from collections import deque

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sq = deque()
        for i in s:
            if i == "#":
                if len(sq)>0:
                    sq.pop()
            else:
                sq.append(i)
        
        tq = deque()
        for i in t:
            if i == "#":
                if len(tq)>0:
                    tq.pop()
            else:
                tq.append(i)

        if len(sq)!=len(tq):
            return False

        # print(sq)
        # print(tq)
        
        while len(sq)>0 and len(tq)>0:
            if sq.pop() != tq.pop():
                return False
        
        return True