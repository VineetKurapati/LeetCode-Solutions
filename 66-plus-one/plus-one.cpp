class Solution {
public:
    vector<int> plusOne(vector<int>& nums) {
        int n = nums.size();
        int carry = 1;
        for(int i = n-1; i>=0; i--)
        {
            int sum = nums[i] + carry;
            carry = sum/10;
            nums[i] = sum%10;
        }
        if(carry > 0)
        {
            vector<int>res;
            res.push_back(carry);
            for(int i = 0; i < n; i++) {
                res.push_back(nums[i]);
            }
            return res;
        }
        return nums;
    }
};