class Solution {
public:
    int helper(int n )
    {
        int count = 0;
        while(n>0)
        {
            count += 1;
            n = n & (n-1);
        }
        return count;
    }
    vector<int> countBits(int n) {
        vector<int>res(n+1);
        for(int i = 0; i<=n;i++)
        {
           res[i] = helper(i);
        }
        return res;
    }
};