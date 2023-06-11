# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def traverse(p,q):

            if not p and not q:
                return True

            elif (not p and q) or (p and not q):
                return False

            elif p.val != q.val:
                return False
            
            return traverse(p.left,q.left) and traverse(p.right,q.right)

        return traverse(p,q)