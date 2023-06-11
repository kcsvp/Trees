# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # def inorder(root):

        #     if not root:
        #         return 
        #     inorder(root.left)
        #     output.append(root.val)
        #     inorder(root.right)
           
        # output = []

        # inorder(root)
        # return output

        stack = []
        sol = []

        curr = root

        while curr or stack:

            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()

            sol.append(curr.val)
            curr = curr.right

        return sol


            