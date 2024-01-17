#include <iostream>
#include <queue>

using namespace std;

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
     bool isSameTree(TreeNode* p, TreeNode* q) {
       if (!p && !q) {
            return true; // 두 트리가 모두 비어 있으면 같다고 간주
        }
        if (!p || !q) {
            return false; // 둘 중 하나만 비어 있으면 다르다고 간주
        }

        // 현재 노드의 값이 같은지 확인
        if (p->val != q->val) {
            return false;
        }

        // 왼쪽 서브트리와 오른쪽 서브트리를 재귀적으로 비교
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
     }  
};