class Solution {
public:
    TreeNode* helper(vector<int>& nums, int start, int end)
    {
        if (start <= end) // Change from start < end to start <= end
        {
            int mid = start + (end - start) / 2;
            TreeNode* res = new TreeNode(nums[mid]);
            res->left = helper(nums, start, mid - 1);  // Change from 0 to start
            res->right = helper(nums, mid + 1, end);
            return res;
        }
        else
        {
            return nullptr;  // Use nullptr instead of NULL for C++
        }
    }
    
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if (nums.empty())
        {
            return nullptr;
        }
        return helper(nums, 0, nums.size() - 1);
    }
};