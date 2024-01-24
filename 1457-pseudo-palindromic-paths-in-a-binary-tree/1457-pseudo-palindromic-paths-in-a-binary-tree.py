# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def traverse(node, count):
            if not node:
                return 0

            count[node.val] += 1

            # Check if it's a leaf node
            if not node.left and not node.right:
                # Check if the path is pseudo-palindromic
                odd_count = 0
                for c in count:
                    if c % 2 != 0:
                        odd_count += 1
                return 1 if odd_count <= 1 else 0

            left_count = traverse(node.left, count.copy())
            right_count = traverse(node.right, count.copy())

            return left_count + right_count

        return traverse(root, [0] * 10)
