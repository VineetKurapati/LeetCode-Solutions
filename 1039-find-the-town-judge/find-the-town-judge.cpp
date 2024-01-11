class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        if(n == 1) return 1;
        map<int, vector<int>>m;
        map<int,vector<int>>rev;
        for(auto i : trust)
        {
            int first = i[0];
            int second = i[1];
            m[second].push_back(first);
            rev[first].push_back(second);
        }
        for(auto i : m)
        {
            int len = i.second.size();
            if(len == n-1 && rev.find(i.first) == rev.end())
            {
                return i.first;
            }
        }
        return -1;
    }
};