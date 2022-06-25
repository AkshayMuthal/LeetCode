class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def get_str(s):
            char = [0]*26
            for i in s:
                char[ord(i)-97] += 1
            
            ans = ""
            for i in range(26):
                if char[i]>0:
                    while char[i]>0:
                        ans += chr(i+97)
                        char[i] -= 1
            return ans
        
        new_str = [get_str(s) for s in strs]
        ans = []
        for i in range(len(strs)):
            if new_str[i]!="*":
                li = [strs[i]]
                for j in range(i+1, len(strs)):
                    if new_str[i] == new_str[j]:
                        new_str[j] = "*"
                        li.append(strs[j])
                ans.append(li)
        return ans