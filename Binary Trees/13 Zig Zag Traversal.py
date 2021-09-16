class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
                return self.bfs(root)
        
    def bfs(self,root):
        
        from collections import deque
        
        q = deque()
        q.append(root)
        
        result = []
        level  = 0
        
        while q :
            
            lst = []
            
            if level%2 == 0:
                
                for _ in range(len(q)):
                    
                    node = q.popleft()
                    
                    if node:
                        
                        lst.append(node.val)
                        q.append(node.left)
                        q.append(node.right)
            else:
                
                for _ in range(len(q)):
                    
                    node = q.pop()
                    
                    if node:
                        
                        lst.append(node.val)
                        q.appendleft(node.right)
                        q.appendleft(node.left)
                        
            if lst != []:
                result.append(lst)
            level = level + 1
        
        return result