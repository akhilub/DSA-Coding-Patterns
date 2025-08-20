#Approach:BFS

'''
A better approach to this problem should be BFS, traversing from top to bottom level by level.

The time complexity is O(nlogn), and the space complexity is O(n). Where n is the number of nodes in the binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
>>> d = {1:'a', -1:'b', 10:'c', -100:'d'}
>>>
>>> d.items()
dict_items([(1, 'a'), (-1, 'b'), (10, 'c'), (-100, 'd')])

>>> ds = sorted(d.items())
>>> ds
[(-100, 'd'), (-1, 'b'), (1, 'a'), (10, 'c')]

>>> sorted(d.items(), key=lambda l: l[1])
[(1, 'a'), (-1, 'b'), (10, 'c'), (-100, 'd')]
>>> dict(sorted(d.items(), key=lambda l: l[1]))
{1: 'a', 10: 'c', -100: 'd', -1: 'b'}

>>> [v for k,v in sorted(d.items(), key=lambda l: l[0])]
['d', 'b', 'a', 'c']
'''

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q=deque([root,0])
        d = defaultdict(list)
        while q:
            for _ in range(len(q)):
                node,offset = q.popleft()
                d[offset].append(node.val)
                if node.left:
                    q.append((node.left,offset-1))
                if node.right:
                    q.appenf((node.right,offset+1))
        
        return [val for key,val in sorted(d.items())]
    

    