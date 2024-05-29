class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        while len(s) > 1:
            if s[-1] == '0':  # If the last character is '0', the number is even
                s = s[:-1]  # Divide by 2 by removing the last character
            else:  # If the last character is '1', the number is odd
                s = bin(int(s, 2) + 1)[2:]  # Add 1 to the binary number and convert back to binary string
            steps += 1
        return steps
