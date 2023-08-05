class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        if not n:return 
        dp={}
        
        def generate_trees(s,e):
            
            if (s,e) in dp:return dp[(s,e)]
            
            trees=[]
            if s>e:
                trees.append(None)
                return trees
            
            for i in range(s,e+1):
                left_trees=generate_trees(s,i-1)
                right_trees=generate_trees(i+1,e)
                
                
                for lf in left_trees:
                    for rf in right_trees:
                        root=TreeNode(i,lf,rf)
                        trees.append(root)
                
            dp[(s,e)]=trees
            return trees
        
        
        return generate_trees(1,n)
        