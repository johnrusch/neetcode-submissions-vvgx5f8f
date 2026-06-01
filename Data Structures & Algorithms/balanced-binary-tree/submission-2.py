# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        isBalanced = True

        def dfs(node):
            nonlocal isBalanced

            if not node:
                return 0

            right = dfs(node.right)
            left = dfs(node.left)

            if abs(right - left) > 1:
                isBalanced = False

            return max(right, left) + 1

        dfs(root)
        return isBalanced