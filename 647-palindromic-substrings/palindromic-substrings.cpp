#include <string>
using namespace std;

class Solution {
public:
    int count = 0;

    bool isPalindrome(const string& str, int start, int end) {
        while (start < end) {
            if (str[start++] != str[end--]) {
                return false;
            }
        }
        return true;
    }

    void backtrack(const string& s, int start) {
        if (start == s.length()) {
            return;
        }

        for (int end = start; end < s.length(); end++) {
            if (isPalindrome(s, start, end)) {
                count++;
            }
        }

        backtrack(s, start + 1); // Move to the next starting index
    }

    int countSubstrings(string s) {
        backtrack(s, 0);
        return count;
    }
};
