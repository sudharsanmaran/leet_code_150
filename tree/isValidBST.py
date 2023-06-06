from typing import Optional

from tree.Invert_Binary_Tree import TreeNode
from tree.Lowest_Common_Ancestor_of_a_Binary_Search_Tree import create_tree

"""
approach => dfs, all the left node's val must be less then to root's val. Similarly, all the right node's val 
            must be grater then root's val.
            
avoid => checking just parent and child is not enough
"""


class Solution:
    def isValidBST(self, node: Optional[TreeNode]) -> bool:
        def valid(node: Optional[TreeNode], left_bound, right_bound) -> bool:
            if not node:
                return True

            if not left_bound < node.val < right_bound:
                return False

            return valid(node.left, left_bound, node.val) and valid(node.right, node.val, right_bound)

        return valid(node, -float('inf'), float('inf'))


if __name__ == '__main__':
    # _tree = create_tree()
    tree = TreeNode(5)
    tree.left = TreeNode(1)
    tree.right = TreeNode(7)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(8)

    solution = Solution()
    print(solution.isValidBST(tree))
