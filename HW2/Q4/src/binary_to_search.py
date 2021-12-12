import Q4


def storeInorder(root, inorder):
    # Base Case
    if root is None:
        return

        # First store the left subtree
    storeInorder(root.left, inorder)

    # Copy the root's data
    inorder.append(root.data)

    # Finally store the right subtree
    storeInorder(root.right, inorder)


# A helper function to count nodes in a binary tree
def countNodes(root):
    if root is None:
        return 0

    return countNodes(root.left) + countNodes(root.right) + 1


# Helper function that copies contents of sorted array
# to Binary tree
def arrayToBST(arr, root):
    # Base Case
    if root is None:
        return

        # First update the left subtree
    arrayToBST(arr, root.left)

    # now update root's data delete the value from array
    root.data = arr[0]
    arr.pop(0)

    # Finally update the right subtree
    arrayToBST(arr, root.right)


# This function converts a given binary tree to BST
def binaryTreeToBST(root):
    # Base Case: Tree is empty
    if root is None:
        return

        # Count the number of nodes in Binary Tree so that
    # we know the size of temporary array to be created
    n = countNodes(root)

    # Create the temp array and store the inorder traversal
    # of tree
    arr = []
    storeInorder(root, arr)

    # Sort the array
    arr.sort()

    # copy array elements back to binary tree
    arrayToBST(arr, root)


tree = Q4.fileopen()
Len = len(tree)
root = Q4.buildtree(tree, 0, Len - 1)
binaryTreeToBST(root)
print("Binary Search Tree is successfully built.")
