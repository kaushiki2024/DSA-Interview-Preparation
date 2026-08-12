# LeetCode 144: Binary Tree Preorder Traversal
#
# Approach:
# Root->Left->Right
#
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root, result):
    if root == None:
        return

    result.append(root.val)

    preorder(root.left, result)
    preorder(root.right, result)


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        preorder(root, result)

        return result


# Main function
if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    obj = Solution()
    print(obj.preorderTraversal(root))