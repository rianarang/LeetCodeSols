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
    TreeNode* invertTree(TreeNode* root) {
        //empty tree and one element tree
        if(root == nullptr) return nullptr;
        if(root->right == nullptr && root ->left == nullptr) 
            return root;
        //at least one child
        TreeNode* rs = invertTree(root->right);
        TreeNode* ls = invertTree(root->left);
        
        root->left = rs;
        root->right = ls;
        return root;
    }
};