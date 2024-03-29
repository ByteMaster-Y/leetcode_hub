#include <iostream>
#include <algorithm>
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
    int height(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }
        
        int left_height = height(node->left);
        int right_height = height(node->right);
        return 1 + max(left_height, right_height);
    }
    
    bool isBalanced(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }
        
        int left_height = height(root->left);
        int right_height = height(root->right);
        
        if (abs(left_height - right_height) <= 1 && isBalanced(root->left) && isBalanced(root->right)){
            return true;
        }
        
        return false;
        
    }
};