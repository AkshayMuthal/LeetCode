class Node:
    def __init__(self):
        # self.char = char
        self.next = [None]*26
        self.word_end = False

class Solution:
    def get_three_words(self, word, node, ans):
        if self.rl>=3:
            return ans
        if node.word_end:
            ans.append(word)
            self.rl += 1
        if self.rl<3:
            for i in range(26):
                tn = node.next[i]
                if tn!=None:
                    ans = self.get_three_words(word+self.ca[i], tn, ans)
        return ans
        
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        self.start_list = [None]*26
        
        self.ca = []
        for i in range(26):
            self.ca.append(chr(97+i))
        
        for product in products:
            curr_list = self.start_list
            for char in product:
                val = ord(char)-97
                if curr_list[val]==None:
                    curr_list[val] = Node()
                prev = curr_list[val]
                curr_list = curr_list[val].next
            prev.word_end = True
        
        word = ""
        temp = None
        curr_list = self.start_list
        ans = []
        for ind, char in enumerate(searchWord):
            word += char
            val = []
            
            if curr_list!=None:
                temp = curr_list[ord(char)-97]
            if temp != None:
                self.rl = 0
                val = self.get_three_words(word, temp, val)
                curr_list = temp.next
            else:
                curr_list = None
            ans.append(val)
        return ans
        