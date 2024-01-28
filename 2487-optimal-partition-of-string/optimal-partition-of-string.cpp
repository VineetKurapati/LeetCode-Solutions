class Solution {
public:
    int partitionString(string s) {
        int i = 0;
        int n = s.length();
        map<char, int>m;
        int count = 0;
        while(i<n)
        {
            if(m[s[i]] == 0)
            {
                m[s[i]] = 1;
                i++;
            }
            else
            {
                count++;
                m.clear();
            }
        }
        return count + 1;
    }
};