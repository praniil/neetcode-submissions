# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            qlen = len(queue)
            test = []
            for i in range(qlen):
                node = queue.popleft()
                if node:
                    test.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if test:
                res.append(test)
            
        return res