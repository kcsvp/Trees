# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        nums = []

        def inorder(root):
            if root:
                if inorder(root.left):
                    if not nums or nums[-1] < root.val:
                        nums.append(root.val)
                    else:
                        return False
                    if not inorder(root.right):
                        return False
                else:
                    return False
            return True
        
        return inorder(root)


