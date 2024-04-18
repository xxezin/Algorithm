from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root:Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        q = deque([root])
        depth = 0
    
        while q:
            depth += 1
            # 큐 연산 추출 노드의 자식 노드 삽입
            for _ in range(len(q)):
                cur_root = q.popleft()
                if cur_root.left:
                    q.append(cur_root.left)
                if cur_root.right:
                    q.append(cur_root.right)
    
        # BFS 반복 횟수 == 깊이
        return depth

Solution.maxDepth([3,9,20,None,None,15,7])