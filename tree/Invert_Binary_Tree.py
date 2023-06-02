from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return

    # Swap the left and right children
    root.left, root.right = root.right, root.left

    # Recursively invert the left and right subtrees
    invertTree(root.left)
    invertTree(root.right)

    #  return root
    return root


def print_tree(root, level=0):
    if root:
        print_tree(root.right, level + 1)
        print("    " * level + str(root.val))
        print_tree(root.left, level + 1)


def create_binary_tree():
    # Create a binary tree for testing
    #      4
    #    /   \
    #   2     7
    #  / \   / \
    # 1   3 6   9
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(7)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(9)
    return tree


if __name__ == '__main__':
    tree = create_binary_tree()

    # Invert the tree
    inverted_tree = invertTree(tree)

    print("Inverted tree:")
    print_tree(inverted_tree)
