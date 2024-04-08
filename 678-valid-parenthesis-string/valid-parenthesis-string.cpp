#include <string>
#include <stack>

class Solution {
public:
    bool checkValidString(std::string s) {
        int low = 0, high = 0;
        for (char c : s) {
            if (c == '(') {
                low++;
                high++;
            } else if (c == ')') {
                if (low > 0) low--;
                high--;
            } else { // c == '*'
                if (low > 0) low--;
                high++;
            }
            if (high < 0) return false; // Too many ')'s
        }
        return low == 0;
    }
};
