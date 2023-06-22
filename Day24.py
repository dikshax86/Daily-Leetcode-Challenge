class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.ans=float(inf)
        self.val=float(-inf)
        
        def min_diff(root):
            if not root:return 
            
            min_diff(root.left)
            
            self.ans=min(self.ans,abs(root.val-self.val))
            self.val=root.val
            
            min_diff(root.right)
        
        
        min_diff(root)
        return self.ans