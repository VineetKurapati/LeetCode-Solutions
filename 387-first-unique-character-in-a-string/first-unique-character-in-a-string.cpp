class Solution {
public:
    int firstUniqChar(string s) {
        map<char,int>m;
        int n = s.length();
        for(auto ch : s)
        {
            m[ch]++;
        }
        for(int i = 0; i <n;i++)
        {
            if(m[s[i]] == 1) return i;
        }
        return -1;
    }
};