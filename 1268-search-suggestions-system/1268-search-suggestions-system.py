class Node:
    def __init__(self, char):
        self.char = char
        self.next = [None]*26
        self.word_end = False

class Solution:
    def get_word(self, node, w):
        if node!= None:
            if node.word_end:
                print(w)
                return

            for i in range(26):
                if node.next[i] != None:
                    self.get_word(node.next[i], w+node.next[i].char)

    
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
                    ans = self.get_three_words(word+tn.char, tn, ans)
        return ans
        
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        self.start_list = [None]*26
        
        for product in products:
            node = None
            curr_list = self.start_list
            prod_len = len(product)
            node = None
            for char in product:
                curr_list[ord(char)-97] = Node(char) if curr_list[ord(char)-97] == None else curr_list[ord(char)-97]
                node = curr_list[ord(char)-97]
                prev = node
                curr_list = curr_list[ord(char)-97].next
            prev.word_end = True
        
        # for i in range(26):
        #     if self.start_list[i] != None:
        #         self.get_word(self.start_list[i], self.start_list[i].char)
        
        word = ""
        temp = None
        curr_list = self.start_list
        ans = []
        # print(len(searchWord))
        for ind, char in enumerate(searchWord):
            word += char
            temp = curr_list[ord(char)-97] if curr_list!=None else None
            val = []
            if temp != None:
                self.rl = 0
                val = self.get_three_words(word, temp, [])
                curr_list = temp.next
            else:
                # print(ind)
                curr_list = None
            ans.append(val)
        
        # for v in ans:
        #     print(v)
            
        return ans
        