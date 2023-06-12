# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return []

        q  = deque()
        q.append(root)
        None_found = False

        while q:
            curr = q.popleft()
            if curr is None and not None_found:
                None_found = True
            if curr and None_found:
                return False

            if curr is None:
                continue

            if curr.left:
                q.append(curr.left)
            else:
                q.append(None)
            if curr.right:
                q.append(curr.right)
            else:
                q.append(None)
            

        return True
            