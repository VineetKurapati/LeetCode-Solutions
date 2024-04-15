/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int res = 0;
    void dfs(TreeNode* root, int count)
    {
        if(root == NULL)
        {
            return;
        }
        count = (count*10) + root->val;
        if(!root->left && !root->right)
        {
            res+=count;
            return;
        }
        dfs(root->left, count);
        dfs(root->right, count);
    }
    int sumNumbers(TreeNode* root) {
        if(!root)
        {
            return 0;
        }
        dfs(root, 0);
        return res;
    }
};