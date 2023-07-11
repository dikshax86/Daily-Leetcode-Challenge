class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        if not root:return []
        dic=collections.defaultdict(TreeNode)
        visited=[]
        
        def dfs(node,parent):
            if not node:return
            
            dic[node]=parent
            dfs(node.left,node)
            dfs(node.right,node)
            
        def find_nodes(tnode,dis):
            if not tnode:return []
            
            if tnode in visited:return []
    
            visited.append(tnode)

            if dis==0:
                return [tnode.val]

            return find_nodes(tnode.left,dis-1)+find_nodes(tnode.right,dis-1)+find_nodes(dic[tnode],dis-1)
            
            
            
        dfs(root,"")
        return find_nodes(target,k)
            