class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n = word1.length();
        int m = word2.length();
        int i = 0;
        int size = min(n, m);
        string ans = "";
        while(i < size)
        {
            ans+= word1[i];
            ans+= word2[i];
            i+=1;
        }
        while(i < n)
            {
                ans+= word1[i];
                i+=1;
            }
        while(i < m)
        {
            ans+= word2[i];
            i+=1;
        }
        return ans;
    }
};