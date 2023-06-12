# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        sol = None


        # def lca(root):
        #     nonlocal sol
        #     if root:
        #         left = True if lca(root.left) else False
        #         right = True if lca(root.right) else False
        #         if left and right and not sol:
        #             sol = root
        #         elif (left or right) and (root == p or root == q) and not sol:
        #             sol = root 
        #         elif root == p or root == q:
        #             return True
        #         return left or right
        #     return False


        # def lca(root):
        #     nonlocal sol
        #     if root:
                
        #         if root.val == p.val:
        #             if p.val < q.val:
        #                 left = True
        #                 right = True if lca(root.right) else False
        #             else:
        #                 right = True
        #                 left = True if lca(root.left) else False
                    
        #         elif root.val == q.val:
        #             if p.val < q.val:
        #                 right = True
        #                 left = True if lca(root.left) else False
        #             else:
        #                 left = True
        #                 right = True if lca(root.right) else False
        #         else:
        #             left = True if lca(root.left) else False
        #             right = True if lca(root.right) else False

        #         if left and right and not sol:
        #             sol = root
        #         return left or right

                
        #     return False

        # lca(root)

        def lca(root):

            if root:

                if root.val < p.val and root.val < q.val:
                    return lca(root.right)

                elif root.val > p.val and root.val  > q.val:
                    return lca(root.left)

                else:
                    return root


        return lca(root)