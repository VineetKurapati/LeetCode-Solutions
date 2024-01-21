class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 0) return 0;
        if(nums.size() == 1) return nums[0];
        if(nums.size() == 2) return max(nums[0],nums[1]);
        int n = nums.size();
        vector<int>dp(n, 0);
        dp[0] = nums[0];
        dp[1] = nums[1];
        dp[2] = max(nums[0]  + nums[2] , nums[1]);
        for(int i = 3;i <n; i++)
        {
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i];
        }
        int res = INT_MIN;
        for(auto num: dp)
        {
            res = max(num, res);
        }
        return res;

    }
};