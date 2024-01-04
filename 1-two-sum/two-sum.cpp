class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int>m;
        int n = nums.size();
        for(int i = 0; i<n;i++)
        {
            int check = target - nums[i];
            if(m.find(check) != m.end())
            {
                return {m[check], i};
            }
            else
            {
                m[nums[i]] = i;
            }
        }
        return {-1,-1};
    }
};