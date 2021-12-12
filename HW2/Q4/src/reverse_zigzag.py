import Q4


def HeightOfTree(root):
    if root is None:
        return 0

    # Compute the height of each subtree
    lheight = HeightOfTree(root.left)
    rheight = HeightOfTree(root.right)

    # Return the maximum of two
    return max(lheight + 1, rheight + 1)


# Function to Print nodes from right to left
def Print_Level_Right_To_Left(root, level):
    if root is None:
        return

    if level == 1:
        print(root.data, end=" ")

    elif level > 1:
        Print_Level_Right_To_Left(root.right,
                                  level - 1)
        Print_Level_Right_To_Left(root.left,
                                  level - 1)

    # Function to Print nodes from left to right


def Print_Level_Left_To_Right(root, level):
    if root is None:
        return

    if level == 1:
        print(root.data, end=" ")

    elif level > 1:
        Print_Level_Left_To_Right(root.left,
                                  level - 1)
        Print_Level_Left_To_Right(root.right,
                                  level - 1)

    # Function to print Reverse


# zigzag of a Binary tree
def PrintReverseZigZag(root):
    # Flag is used to mark the
    # change in level
    flag = 1

    # Height of tree
    height = HeightOfTree(root)

    for i in range(height, 0, -1):

        # If flag value is one print
        # nodes from right to left
        if flag == 1:
            Print_Level_Right_To_Left(root, i)

            # Mark flag as zero so that next time
            # tree is traversed from left to right
            flag = 0

        # If flag is zero print nodes
        # from left to right
        elif flag == 0:
            Print_Level_Left_To_Right(root, i)

            # Mark flag as one so that next time
            # nodes are printed from right to left
            flag = 1


tree = Q4.fileopen()
Len = len(tree)
root = Q4.buildtree(tree, 0, Len - 1)
PrintReverseZigZag(root)
