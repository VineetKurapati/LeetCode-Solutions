class Solution {
public:
    bool isPalindrome(int x) {
        long num = 0;
        long num1 = x;
        while(x > 0)
        {
            num = (num*10) + x % 10;
            x/=10;
        }
        return num == num1;
    }
};