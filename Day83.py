# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return 
        queue=[]
        queue.append(root)
        max_val=-float('inf')
        li=[]
        
        while queue:
            
            for i in range(len(queue)):
                root=queue.pop(0)
                max_val=max(max_val,root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            li.append(max_val)
            
            max_val=-float('inf')
        
        return li
        