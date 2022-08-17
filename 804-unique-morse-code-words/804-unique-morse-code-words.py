class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        li = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        hs = set()
        for word in words:
            s = ""
            for c in word:
                s += li[ord(c)-97]
            hs.add(s)
        return len(hs)