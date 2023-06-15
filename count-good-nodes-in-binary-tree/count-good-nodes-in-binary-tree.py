# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        path = [float('-inf')]
        sol = 0

        def dfs(root,mx_val):
            nonlocal sol

            if root:
                if root.val >= mx_val:
                    sol += 1

                mx_val = max(mx_val,root.val)
                dfs(root.left,mx_val)
                dfs(root.right,mx_val)
                # path.pop()

        dfs(root,float('-inf'))

        return sol
