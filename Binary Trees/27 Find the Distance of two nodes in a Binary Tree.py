class Solution:
    
    def findDist(self,root,a,b):
        
        self.lca = None
    
        self.find_lca(root,a,b)
        
        return self.distance(root,a,b)
        
    def find_lca(self,root,p,q): 
        
        if not root:       
            return False
        
        if root.data == p or root.data == q: 
            
            mid = True
        else:
            mid = False
            
        left  = self.find_lca(root.left,p,q) 
        
        right = self.find_lca(root.right,p,q)
        
        if mid + right + left >= 2:
            self.lca = root.data
        
        return (mid or left or right)     
    
    def distance(self,root,a,b):
        
        from collections import deque
        
        q = deque()
        q.append(root)
        
        dist_node1,dist_node2,dist_lca = -1, -1, -1
        depth = 0
        
        while q:
            
            for _ in range(len(q)):
                
                node = q.popleft()
                
                if node.data == self.lca:
                    dist_lca = depth
                    
                if node.data == a:
                    dist_node1 = depth
                    
                if node.data == b:
                    dist_node2 = depth
                    
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                    
            depth = depth + 1
        
        return ( dist_node1 + dist_node2 - 2*(dist_lca) )