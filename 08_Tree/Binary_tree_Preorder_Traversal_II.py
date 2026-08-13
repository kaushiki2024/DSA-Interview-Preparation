# LeetCode 107: Binary Tree Level Order Traversal II
#
# Approach:
# Level Order Traversal using Queue
# Store each level in a separate list and reverse the result
#
# Time Complexity: O(n^2)
# Space Complexity: O(n)

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = []

        if root:
            q.append(root)

        while len(q) != 0:
            level = []

            for i in range(len(q)):
                node = q.pop(0)

                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            result.append(level)

        result.reverse()

        return result


# Main function
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    obj = Solution()
    print(obj.levelOrderBottom(root))