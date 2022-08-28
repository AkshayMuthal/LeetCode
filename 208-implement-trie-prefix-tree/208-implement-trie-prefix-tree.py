class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.end_of_word = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            if char not in curr.childrens:
                curr.childrens[char] = TrieNode()
            curr = curr.childrens[char]
        
        curr.end_of_word = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for char in word:
            if char not in curr.childrens:
                return False
            curr = curr.childrens[char]
        
        return curr.end_of_word
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for char in prefix:
            if char not in curr.childrens:
                return False
            curr = curr.childrens[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)