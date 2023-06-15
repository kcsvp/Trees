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

        def dfs(root):
            nonlocal sol

            if root:
                if root.val >= path[-1]:
                    sol += 1

                path.append(max(path[-1],root.val))
                dfs(root.left)
                dfs(root.right)
                path.pop()

        dfs(root)

        return sol
