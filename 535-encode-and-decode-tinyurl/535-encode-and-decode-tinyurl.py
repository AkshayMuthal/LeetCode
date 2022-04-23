class Codec:
    all_chars = string.ascii_letters + string.digits
    codeDB, urlDB = defaultdict(), defaultdict()
    short_size = 6
    
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
