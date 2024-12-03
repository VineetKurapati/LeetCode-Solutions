class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        result = []
        prev = 0  # To track the start of the next substring

        for space in spaces:
            result.append(s[prev:space])  # Append the substring up to the current space index
            result.append(" ")           # Append the space
            prev = space                 # Update `prev` to the current space index

        result.append(s[prev:])          # Append the remaining part of the string
        return "".join(result)           # Join all parts together
