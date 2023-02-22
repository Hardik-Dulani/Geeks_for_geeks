# Given a binary tree, connect the nodes that are at the same level.
# The structure of the tree Node contains an addition nextRight pointer for this purpose.

# Initially, 
# all the nextRight pointers point to garbage values. 
# Your function should set these pointers to point next right for each node.

#User function Template for python3


'''
:param root: root of the given tree
:return: none, just connect accordingly.
{
    # Node Class:
    class Node:
        def __init__(self,val):
            self.data = val
            self.left = None
            self.right = None
            self.nextRight = None
}
'''
from queue import Queue
class Solution:
    def connect(self, root):
        curr, nxt = [root], []
        while curr:
            n = len(curr)
            for i in range(n-1):
                curr[i].nextRight = curr[i+1]
                if curr[i].left:
                    nxt.append(curr[i].left)
                if curr[i].right:
                    nxt.append(curr[i].right)
            if curr[n-1].left:
                nxt.append(curr[n-1].left)
            if curr[n-1].right:
                nxt.append(curr[n-1].right)
            curr, nxt = nxt, []
