from tree.Invert_Binary_Tree import TreeNode

"""
problem => A node in a binary tree is considered a "good" node if it has a greater value than all the nodes present on 
           the path from the node to that node.
   
approach => traverse tree in dfs manner and pass max value of the node's so far for every node.
            If any node is bigger or equal to max value then increment good nodes counter
            
difficulties => have to pass different max values for left and right side from node
   
"""


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """recursion"""
        return self.get_good_nodes(root, -float('inf'))

    def get_good_nodes(self, root: TreeNode, max_node_val: int) -> int:
        no_of_good_nodes = 0
        if not root:
            return no_of_good_nodes

        # update good nodes
        if max_node_val <= root.val:
            no_of_good_nodes += 1

        # update max val
        max_node_val = max(max_node_val, root.val)

        no_of_good_nodes += self.get_good_nodes(root.left, max_node_val)
        no_of_good_nodes += self.get_good_nodes(root.right, max_node_val)

        return no_of_good_nodes

    def good_nodes_1(self, root: TreeNode) -> int:
        """iterative"""
        if not root:
            return 0

        stack = [(root, float('-inf'))]  # to store apt max value
        no_of_good_nodes = 0

        while stack:
            node, max_value = stack.pop()

            if node.val >= max_value:
                no_of_good_nodes += 1

            max_value = max(max_value, node.val)

            if node.left:
                stack.append((node.left, max_value))
            if node.right:
                stack.append((node.right, max_value))

        return no_of_good_nodes


def build_tree(nums, index):
    if index >= len(nums) or nums[index] is None:
        return None

    root = TreeNode(nums[index])
    root.left = build_tree(nums, 2 * index + 1)
    root.right = build_tree(nums, 2 * index + 2)

    return root


if __name__ == '__main__':
    # Tree:
    #       6
    #    /     \
    #   2       10
    #  / \     /  \
    # 0   4   7    11
    #    / \   \
    #   3   5    8
    # _tree = create_tree()
    #
    tree = TreeNode(3)
    tree.left = TreeNode(1)
    tree.left.left = TreeNode(3)
    tree.right = TreeNode(4)
    tree.right.left = TreeNode(1)
    tree.right.right = TreeNode(5)

    # nums = [-1, 5, -2, 4, 4, 2, -2, None, None, -4, None, -2, 3, None, -2, 0, None, -1, None, -3, None, -4, -3, 3,
    #         None, None, None, None, None, None, None, 3, -3]
    # node = build_tree(nums, 0)

    solution = Solution()
    print(solution.goodNodes(tree))
