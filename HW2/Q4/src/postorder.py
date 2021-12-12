import Q4


def postorder(root):
    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.data) + "->", end='')
        return 1


tree = Q4.fileopen()
Len = len(tree)
root = Q4.buildtree(tree, 0, Len - 1)