# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

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
                if n%2 == 0:
                    sol.append(curr_level)
                else:
                    sol.append(curr_level[::-1])
                curr_level = [curr.val]
                n += 1
            else:
                curr_level.append(curr.val)
            if curr.left:
                q.append((curr.left,level + 1))
            if curr.right:
                q.append((curr.right,level + 1))
            
        if curr_level:
            if n%2 == 0:
                sol.append(curr_level)
            else:
                sol.append(curr_level[::-1])

        return sol