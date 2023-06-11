# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        def inorder(root):
            nonlocal i,k
            if root:
                left = inorder(root.left)
                if left is not None:
                    return left
                i += 1
                if i == k:
                    return root.val
                right = inorder(root.right)
                if right is not None:
                    return right
            return None
        return inorder(root)
                

