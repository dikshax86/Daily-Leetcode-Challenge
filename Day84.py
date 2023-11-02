# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def dfs(root):
            
            if not root:return (0,0)
            
            if not root.left and not root.right: 
                self.ans+=1
                return (root.val,1)
            
            left=dfs(root.left)
            right=dfs(root.right)
            
            sub_tree_sum=left[0]+right[0]+root.val
            sub_tree_size=left[1]+right[1]+1
            
            avg=sub_tree_sum//sub_tree_size
            
            if avg==root.val:
                self.ans+=1
            
            return (sub_tree_sum,sub_tree_size)
    
        dfs(root)
        
        return self.ans