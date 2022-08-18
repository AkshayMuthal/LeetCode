class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = {}
        for i in arr:
            counter[i] = counter.get(i, 0)+1
        counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
        req_len = len(arr)/2
        occurances = 0
        cnt = 0
        
        for k, v in counter.items():
            if occurances>=req_len:
                return cnt
            occurances += v
            cnt += 1
        return cnt