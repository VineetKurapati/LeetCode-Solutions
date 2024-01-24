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
private:
    bool isPalindromic(const unordered_map<int,int>& freq)
    {
        int oddCount = 0;
        for(const auto& it : freq)
        {
            if(it.second % 2  == 1)
            {
                oddCount++;
            }
            if(oddCount > 1) return false;
        }
        return true;
    }
    void dfs(TreeNode* root, unordered_map<int,int>& freq, int& fnl)
    {
        if(root == NULL) return;
        freq[root->val]++;
        if(root->left == NULL && root->right == NULL)
        {
            if(isPalindromic(freq))
            {
                fnl++;
            }
        }
        dfs(root->left, freq, fnl);
        dfs(root->right, freq, fnl);
        freq[root->val]--;
        if(freq[root->val] == 0)
        {
            freq.erase(root->val);
        }
    }
public:
    int pseudoPalindromicPaths (TreeNode* root) {
        int fnl = 0;
        unordered_map<int,int>m;
        dfs(root, m, fnl);
        return fnl;
    }
};