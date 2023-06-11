# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        sol = None

        def lca(root):
            nonlocal sol
            if root:
                left = True if lca(root.left) else False
                right = True if lca(root.right) else False
                if left and right and not sol:
                    sol = root
                elif (left or right) and (root == p or root == q) and not sol:
                    sol = root 
                elif root == p or root == q:
                    return True
                return left or right
            return False

        lca(root)
        return sol