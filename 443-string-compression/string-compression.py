from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        result_index = 0
        current_char = chars[0]
        count = 1

        for i in range(1, len(chars)):
            if chars[i] == current_char:
                count += 1
            else:
                chars[result_index] = current_char
                result_index += 1

                if count > 1:
                    count_str = str(count)
                    for digit in count_str:
                        chars[result_index] = digit
                        result_index += 1

                current_char = chars[i]
                count = 1

        chars[result_index] = current_char
        result_index += 1

        if count > 1:
            count_str = str(count)
            for digit in count_str:
                chars[result_index] = digit
                result_index += 1

        chars[result_index:] = []  # Remove any remaining characters

        return result_index
