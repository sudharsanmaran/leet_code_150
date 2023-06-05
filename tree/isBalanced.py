from typing import Optional, Tuple

from tree.Invert_Binary_Tree import TreeNode

"""approach
1. find left and right height for every node, if abs( left_height - right_height) <= 1 then it is balanced
1.1 to make it efficient we find height from bottoms up post-order traversal
"""


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node: Optional[TreeNode]) -> Tuple[bool, int]:
            if not node:
                # empty node considered as balanced
                return True, 0

            left_balanced, left_height = check_balance(node.left)
            right_balanced, right_height = check_balance(node.right)

            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            height = max(left_height, right_height) + 1

            return balanced, height

        if not root:
            return True

        return check_balance(root)[0]

    def diameter(self, root: TreeNode) -> int:

        def get_height(node):
            if not node:
                return 0

            left_height = get_height(node.left)
            right_height = get_height(node.right)

            cur_diameter = left_height + right_height
            self.max_diameter = max(self.max_diameter, cur_diameter)

            # return current node height
            return max(left_height, right_height) + 1

        self.max_diameter = 0
        get_height(root)
        return self.max_diameter


if __name__ == '__main__':
    obj = Solution()
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(10)
    tree.right.right = TreeNode(50)

    print(obj.diameter(tree))
