#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int countSubstrings(string s) {
        int n = s.length();
        vector<vector<int>> dp(n, vector<int>(n, 0)); // Initialize dp table with dimensions n x n

        // Step 1: Base case - single characters are palindromes
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }

        // Step 2: Fill dp table for substrings of length 2
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) {
                dp[i][i + 1] = 1;
            }
        }

        // Step 3: Fill dp table for substrings of length greater than 2
        for (int len = 3; len <= n; len++) { // Iterate over all possible lengths of substrings
            for (int i = 0; i <= n - len; i++) { // Iterate over all possible starting indices
                int j = i + len - 1; // Ending index of the current substring
                if (s[i] == s[j] && dp[i + 1][j - 1]) { // Check if the ends are equal and inner substring is a palindrome
                    dp[i][j] = 1; // Mark the current substring as a palindrome
                }
            }
        }

        // Step 4: Count the palindromic substrings
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                count += dp[i][j];
            }
        }

        return count;
    }
};
