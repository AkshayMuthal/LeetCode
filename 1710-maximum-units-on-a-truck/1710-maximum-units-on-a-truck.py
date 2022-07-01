class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        b = sorted(boxTypes, key=lambda box: box[1], reverse=True)
        # print(b)
        tot = 0
        for i in b:
            if truckSize >= i[0]:
                tot += i[0]*i[1]
                truckSize -= i[0]
            elif 0<truckSize<i[0]:
                # print(truckSize,i[1])
                tot += truckSize*i[1]
                truckSize = 0
            elif truckSize == 0:
                break
        return tot