class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_binary_tree(root, result=None):
    if result is None:
        result = []

    if root:
        result.append(root.value)
        dfs_binary_tree(root.left, result)
        dfs_binary_tree(root.right, result)

    return result

# Example Usage:
# Constructing a binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform DFS on the binary tree
result = dfs_binary_tree(root)
print("DFS Result:", result)
