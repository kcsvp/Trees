# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        sol = []
        # def postorder(root):
        #     if root:
        #         postorder(root.left)
        #         postorder(root.right)
        #         sol.append(root.val)
        
        # postorder(root)

        if not root:
            return []

        stack = [root]
        temp = []

        while stack:

            curr = stack.pop()
            temp.append(curr.val)

            if curr.left:
                stack.append(curr.left)

            if curr.right:
                stack.append(curr.right)

        while temp:
            sol.append(temp.pop())
        return sol