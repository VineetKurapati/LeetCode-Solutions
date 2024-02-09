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
    int count = 0;
    void dfs(TreeNode* root, int max_val)
    {
        if(!root) return;
        int val = root->val;
        if(val >= max_val)
        {
            count+=1;
            max_val = max(val, max_val);
        }
        if(root->left)
        {
            dfs(root->left, max_val);
        }
        if(root->right)
        {
            dfs(root->right, max_val);
        }
    }
    int goodNodes(TreeNode* root) {
        dfs(root, root->val);
        return count;
    }
};