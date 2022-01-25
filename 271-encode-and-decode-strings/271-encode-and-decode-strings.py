class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        output = ''
        for s in strs:
            output = output + str(len(s)).zfill(3) + s
        return output 
    
    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        i, L, output = 0, len(s), []
        while True:
            if len(s) == 0: break
            # read 3 bytes
            length = int(s[:3])
            # strip 3 bytes
            s = s[3:]
            # append output with the length
            output.append(s[:length])
            # strip length bytes
            s = s[length:]
        return output  
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))