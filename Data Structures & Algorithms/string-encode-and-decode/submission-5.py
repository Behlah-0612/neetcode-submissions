class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded = []
        for s in strs:
            # Prefix each string with its length and a delimiter
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        
        decoded = []
        i = 0
        
        while i < len(s):
            # Find where the delimiter '#' is to parse the length
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract the length of the upcoming string
            length = int(s[i:j])
            
            # The actual string starts right after '#'
            start = j + 1
            end = start + length
            
            # Extract the string and add it to our result
            decoded.append(s[start:end])
            
            # Move the pointer to the start of the next encoded block
            i = end
            
        return decoded