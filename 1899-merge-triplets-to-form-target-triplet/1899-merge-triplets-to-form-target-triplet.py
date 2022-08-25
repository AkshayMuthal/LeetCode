class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        indices = []
        for i, triplet in enumerate(triplets):
            if (triplet[0] == target[0] or triplet[1] == target[1] or triplet[2] == target[2]) and (triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]):
                indices.append(i)
        
        ans = [0, 0, 0]
        for i in indices:
            ans[0] = max(ans[0], triplets[i][0])
            ans[1] = max(ans[1], triplets[i][1])
            ans[2] = max(ans[2], triplets[i][2])
            if ans == target:
                return True
        return False
        