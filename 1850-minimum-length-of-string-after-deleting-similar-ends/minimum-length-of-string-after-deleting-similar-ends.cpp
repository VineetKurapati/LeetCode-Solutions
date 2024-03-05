class Solution {
public:
    int minimumLength(string s) {
        int n = s.length();
        if(n == 1)
        {
            return 1;
        }
        int begin = 0;
        int end = n-1;
        while(begin < end && s[begin] == s[end])
        {
            char c = s[begin];
            while(begin <= end && s[begin] == c)
            {
                begin++;
            }
            while(end > begin && s[end] == c)
            {
                end--;
            }
        }
        return end - begin + 1;
    }
};