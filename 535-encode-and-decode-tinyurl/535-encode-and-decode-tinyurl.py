class Codec:
    all_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q','r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    short_size = 7
    codeDB, urlDB = {}, {}
    
    def hash(self):
        return "".join(random.choice(self.all_chars) for i in range(self.short_size))
        

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.urlDB:
            return self.urlDB[longUrl]
        code = self.hash()
        while code in self.codeDB:
            code = self.hash()
        self.codeDB[code] = longUrl
        self.urlDB[longUrl] = code
        return code    
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.codeDB[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))  
