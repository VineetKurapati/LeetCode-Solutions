class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int>s;
        for(auto num: nums)
        {
            s.insert(num);
        }
        int count = 0;
        for(auto num: nums)
        {
            if(s.find(num - 1) == s.end() )
            {
                int n = num ;
                int temp = 1;
                while(s.find(n+1) != s.end())
                {
                    n += 1;
                    temp += 1;
                }
                count = max(temp, count);
            }
        }
        return count;
    }
};