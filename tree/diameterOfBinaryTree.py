from typing import Optional

from tree.Invert_Binary_Tree import TreeNode, create_binary_tree

"""initial approach:
1.Max depth of left + right from root node => issue: max diameter may not pass through root node

so we have to calculate diameter for every node possible 
if use pre / in order traversal we end up calculating multiple times for same node

final approach:
1. use post order traversal to calculate diameter so, we can use children node diameter to calculate parent node.
with this approach we only calculating diameter only once for every node.
"""


class Solution:

    def __init__(self):
        self.diameter = 0

    def calculate_diameter(self, root):
        if not root:
            return 0

        left_height = self.calculate_diameter(root.left)
        right_height = self.calculate_diameter(root.right)

        # calculate diameter
        current_diameter = left_height + right_height
        self.diameter = max(self.diameter, current_diameter)

        # return current node height
        return max(left_height, right_height) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.calculate_diameter(root)
        return self.diameter


if __name__ == '__main__':
    obj = Solution()
    print(obj.diameterOfBinaryTree(create_binary_tree()))
