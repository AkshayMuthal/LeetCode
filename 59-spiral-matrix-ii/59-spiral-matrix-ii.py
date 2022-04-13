class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        a = [[0 for i in range(n)] for j in range(n)]
        
        num = 1
        maxLen = math.pow(n, 2)
        
        u, l, r, d = 1, 0, n-1, n-1
        i, j = 0, 0
        
        row = 1
        forw = 1
        down = 1
        
        while num<=maxLen:
            a[i][j] = num
            num+=1
            if row == 1:
                if forw == 1:
                    if j==r:
                        r-=1
                        row = 0
                        down = 1
                        i+=1
                    else:
                        j+=1
                else:
                    if j==l:
                        l+=1
                        row = 0
                        down = 0
                        i-=1
                    else:
                        j-=1
            else:
                if down == 1:
                    if i==d:
                        d-=1
                        row = 1
                        forw = 0
                        j-=1
                    else:
                        i+=1
                else:
                    if i==u:
                        u+=1
                        row = 1
                        forw = 1
                        j+=1
                    else:
                        i-=1
        return a
