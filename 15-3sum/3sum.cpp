class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int target = 0;
        set<vector<int>>s;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for(int i = 0;i<n-2;i++)
        {
            int j = i + 1;
            int k = nums.size() - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == target) {
                    s.insert({nums[i], nums[j], nums[k]});
                    j++;
                    k--;
                } else if (sum < target) {
                    j++;
                } else {
                    k--;
                }
            }
        }
        vector<vector<int>>ans;
        for(auto i : s)
        {
            ans.push_back(i);
        }
        return ans;
    }
};