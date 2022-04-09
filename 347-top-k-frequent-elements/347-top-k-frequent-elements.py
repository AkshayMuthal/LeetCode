class Solution:
    def topKFrequent(self, nums: List[int], ki: int) -> List[int]:
        mp = {}
        for i in nums:
            if i in mp:
                mp[i]+=1
            else:
                mp[i] = 1
        ans = []
        mp = {k: v for k, v in sorted(mp.items(), key=lambda item: item[1], reverse=True)}
        # print(mp2)
        for k, v in mp.items():
            if ki<=0:
                break
            ans.append(k)
            ki-=1
        return ans