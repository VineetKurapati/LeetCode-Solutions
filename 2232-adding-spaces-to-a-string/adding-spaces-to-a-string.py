class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        result = ""
        prev = 0 

        for space in spaces:
            result += s[prev:space]
            result += " "        
            prev = space                
        result += s[prev:]       
        return result 
