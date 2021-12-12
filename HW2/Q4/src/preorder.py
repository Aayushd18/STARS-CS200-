import Q4

def preorder(root):

    if root:
        # Traverse root
        print(str(root.data) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)
        return 1


tree = Q4.fileopen()
Len = len(tree)
root = Q4.buildtree(tree, 0, Len - 1)