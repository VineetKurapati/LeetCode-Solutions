class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int len = 0;
        int res = 0;
        int curr_max = INT_MIN;
        int n = nums.size();
        for(int i = 0; i<n;i++)
        {
           if(nums[i] > curr_max)
           {
             curr_max = nums[i];
             len+=1;
           }
           else
           {
            curr_max = nums[i];
            len = 1;
           }
           res = max(len, res);
        }
        return res;
    }
};