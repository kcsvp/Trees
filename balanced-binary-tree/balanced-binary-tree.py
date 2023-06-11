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

        sol = True

        def checkbalanced(root):
            nonlocal sol
            if root:
                left =  1 + checkbalanced(root.left)

                right = 1 + checkbalanced(root.right)
            
                if abs(left-right)>1:
                    sol = False

                return max(left,right)

            
            return 0

        checkbalanced(root)
        
        return sol

            