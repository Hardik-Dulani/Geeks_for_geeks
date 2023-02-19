# Two of the nodes of a Binary Search Tree (BST) are swapped.
# Fix (or correct) the BST by swapping them back. Do not change the structure of the tree.
# Note: It is guaranteed than the given input will form BST, except for 2 nodes that will be wrong.

class Solution:
    def getBSTNode(self, root, arr):
        if root == None:
            return
        
        self.getBSTNode(root.left, arr)
        arr.append(root.data)
        self.getBSTNode(root.right, arr)
        
    def updateBST(self, node, arr):
        if node == None: 
            return
        
        self.updateBST(node.left, arr)
        node.data = arr.pop(len(arr) - 1)
        self.updateBST(node.right, arr)
        
    
    def correctBST(self, root):
        # code here
        arr = []
        self.getBSTNode(root, arr)
        arr = sorted(arr, reverse=True)
        self.updateBST(root, arr)
        return root
