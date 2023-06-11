# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q  = deque()
        q.append((root,0))

        sol = []
        curr_level = []
        n = 0
        while q:
            curr,level = q.popleft()
            if level!=n:
                sol.append(curr_level)
                curr_level = [curr.val]
                n += 1
            else:
                curr_level.append(curr.val)
            if curr.left:
                q.append((curr.left,level + 1))
            if curr.right:
                q.append((curr.right,level + 1))
            
        if curr_level:
            sol.append(curr_level)

        return sol






