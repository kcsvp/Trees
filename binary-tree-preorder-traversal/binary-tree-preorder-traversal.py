# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        sol = []
        # def preorder(root):

        #     if root:
        #         sol.append(root.val)
        #         preorder(root.left)
        #         preorder(root.right)
        #     return

        # preorder(root)

        stack = []
        curr = root

        while curr or stack:

            while curr:
                sol.append(curr.val)
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            curr = curr.right

        return sol