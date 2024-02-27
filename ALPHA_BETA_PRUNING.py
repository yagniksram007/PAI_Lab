class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children if children is not None else []

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Construct a simple game tree
root = Node(children=[
    Node(children=[
        Node(value=3),
        Node(value=5)
    ]),
    Node(children=[
        Node(value=6),
        Node(value=9)
    ]),
    Node(children=[
        Node(value=1),
        Node(value=2)
    ])
])

# Perform alpha-beta pruning on the game tree
print(alpha_beta_pruning(root, 2, float('-inf'), float('inf'), True))
