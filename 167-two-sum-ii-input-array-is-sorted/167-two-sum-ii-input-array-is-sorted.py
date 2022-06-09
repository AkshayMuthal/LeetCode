class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        le = len(numbers)
        for i in range(le):
            elem = target-numbers[i]
            l = 0
            r = le-1
            mid = -1
            while l<=r:
                mid = int(l+(r-l)/2)
                if numbers[mid] == elem:
                    break
                elif numbers[mid] > elem:
                    r = mid - 1
                else:
                    l = mid + 1
            # print(i, mid, numbers[i], numbers[mid])
            if mid!=-1 and numbers[mid]+numbers[i] == target:
                if mid!=i:
                    return [mid+1, i+1] if mid<i else [i+1, mid+1]
                if numbers[mid-1] == numbers[mid]:
                    return [mid, i+1] if mid-1<i else [i+1, mid]
                if numbers[mid+1] == numbers[mid]:
                    return [mid+2, i+1] if mid+1<i else [i+1, mid+2]
        return None