class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int,int>m;
        int n = nums.size();
        for(auto num : nums)
        {
            m[num]++;
        }
        for(auto i : m)
        {
            if(i.second > n/2)
            {
                return i.first;
            }
        }
        return -1;
    }
};