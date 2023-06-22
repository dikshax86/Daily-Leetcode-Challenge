
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        queue=[root]
        level=0
        
        ans=float(-inf)
        lev=0
        
        while queue:
            sum_value=0
  
            for i in range(len(queue)):
                node=queue.pop(0)
                sum_value+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level+=1
            
            if ans<sum_value:
                ans=sum_value
                lev=level
           
        return lev
                    
        