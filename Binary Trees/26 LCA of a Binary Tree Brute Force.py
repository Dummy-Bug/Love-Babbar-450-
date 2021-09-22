class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return 
        
        global level         # storing the level of every node
        level = dict() 
        
        global ancestors    # hashtable for ancestors of nodes
        ancestors = dict()
        

        self.level_order_traversal(root)
        
        return self.find_lca(p,q)
        
    def level_order_traversal(self,root): # traverse all the nodes and store their ancestors,we can also stop after encountering the two given nodes to reduce the execution time .
        
        from collections import deque
        
        q = deque()
        
        q.append(root)
        
        global level 
        global ancestors
        
        ancestors[root.val] = -1
        
        depth = 0
        
        while q:
            
            for _ in range(len(q)):
                
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                    ancestors[node.left]  = node
                    
                if node.right:
                    q.append(node.right)
                    ancestors[node.right] = node
            
                level[node] = depth
                
            depth = depth + 1
        
        # print(ancestors)
    
    def find_lca(self,p,q):
            
        global level
        global ancestors
        
        if p == q:
            return p
            
        elif level[p] >= level[q]:
            return self.find_lca(ancestors[p],q)
            
        else:
            return self.find_lca(p,ancestors[q])
                
                
                    
                
                
                
                
                
                
        
        