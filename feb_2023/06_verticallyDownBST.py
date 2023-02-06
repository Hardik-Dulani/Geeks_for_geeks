# Given a Binary Search Tree with unique node values and a target value.
# You have to find the node whose data is equal to target and
# return the sum of all descendant node's data which are vertically below the target node.
# Initially, you are at the root node.
# Note: If target node is not present in bst then return -1.

class Solution:
    def dfs(self, root, targetValue, hasFound=False, targetPos=0, currPos=0):
        if root is None:
            return 0
        ans = 0
        if hasFound and targetPos == currPos:
            ans += root.data
        if not hasFound and root.data == targetValue:
            hasFound = True
            targetPos = currPos
            ans += 1
        ans += self.dfs(root.left, targetValue, hasFound, targetPos, currPos - 1)
        ans += self.dfs(root.right, targetValue, hasFound, targetPos, currPos + 1)
        return ans
    def verticallyDownBST(self, root, target):
        return self.dfs(root, target) - 1
