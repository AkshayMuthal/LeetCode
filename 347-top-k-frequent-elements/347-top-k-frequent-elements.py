import heapq

class Solution:
    def topKFrequent(self, nums: List[int], ki: int) -> List[int]:
        hm = defaultdict()
        for i in nums:
            hm[i] = hm.get(i, 0)+1
        
        max_heap = []
        for k, v in hm.items():
            heapq.heappush(max_heap, (-v, k))
        
        res = []
        for i in range(ki):
            res.append(heapq.heappop(max_heap)[1])
        
        return res