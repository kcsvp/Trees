# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        hashmap = dict()
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i

        def bt(in_start,in_end,post_start,post_end):

            if in_start > in_end or post_start > post_end:
                return None

            root = TreeNode(postorder[post_end])
            r_index = hashmap[root.val]
            l_len = r_index - in_start
            r_len = in_end - r_index
            root.left = bt(in_start,in_start + l_len - 1,post_start,post_start + l_len -1)
            root.right = bt(r_index+1,in_end,post_end - r_len,post_end-1)

            return root

        return bt(0,len(inorder)-1,0,len(inorder)-1)