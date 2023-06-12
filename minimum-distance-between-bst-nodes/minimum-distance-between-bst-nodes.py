# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        ans = float('inf')
        prev = []

        def traverse(root):
            nonlocal ans
            nonlocal prev
            if root:
                traverse(root.left)
                if prev:
                    ans = min(abs(prev[-1]-root.val),ans)
                prev.append(root.val)
                traverse(root.right)

        traverse(root)
        return ans