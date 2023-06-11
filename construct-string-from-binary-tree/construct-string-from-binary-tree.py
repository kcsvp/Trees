# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def getstr(root):

            if root:
                s = str(root.val)
                if not root.left and not root.right:
                    return s
                elif root.left:
                    s += '(' + getstr(root.left) + ')'
                elif not root.left:
                    s += '()'
                if root.right:
                    s += '(' + getstr(root.right) + ')'

                return s

            return ''

        return getstr(root)