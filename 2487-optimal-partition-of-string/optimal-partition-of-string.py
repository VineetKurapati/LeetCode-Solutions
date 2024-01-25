class Solution:
    def partitionString(self, s: str) -> int:
        seen_chars = set()
        substr_count = 0

        for char in s:
            if char in seen_chars:
                substr_count += 1
                seen_chars = set()

            seen_chars.add(char)

        # If there are remaining characters in the last substring
        if seen_chars:
            substr_count += 1

        return substr_count
