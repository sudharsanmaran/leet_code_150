from typing import Optional

from tree.Invert_Binary_Tree import TreeNode
from tree.Lowest_Common_Ancestor_of_a_Binary_Search_Tree import create_tree


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder_traversal(root: Optional[TreeNode]):
            if not root:
                return

            inorder_traversal(root.left)
            nodes_val.append(root.val)
            inorder_traversal(root.right)

        nodes_val = []
        inorder_traversal(root)
        return nodes_val[k - 1]

    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            curr = curr.right


if __name__ == '__main__':
    _tree = create_tree()
    sol = Solution()
    print(sol.kth_smallest(_tree, 4))
