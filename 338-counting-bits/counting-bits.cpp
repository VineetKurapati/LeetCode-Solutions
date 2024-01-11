class Solution {
public:
    vector<int> countBits(int n) {
        vector<int>res;
        res.emplace_back(0);
        for(int i = 1; i<=n;i++)
        {
           res.emplace_back(res[i/2] + i % 2);
        }
        return res;
    }
};