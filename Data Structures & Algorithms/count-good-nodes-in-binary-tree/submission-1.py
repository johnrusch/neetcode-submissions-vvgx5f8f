# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node: TreeNode, curr_max: int):
            good_node = 0

            if not node:
                return 0

            if node.val >= curr_max:
                good_node += 1
                curr_max = node.val

            return dfs(node.left, curr_max) + dfs(node.right, curr_max) + good_node

        return dfs(root, float("-inf"))