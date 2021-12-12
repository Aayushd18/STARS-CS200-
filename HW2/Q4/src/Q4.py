class NewNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def fileopen():
    f = open("file.txt", 'r')
    fileread = f.read()
    arr = [x for x in fileread.split(',')]
    f.close()
    return arr


def buildtree(inorder, start, end):
    if start > end:
        return None

    # Find index of the maximum element
    # from Binary Tree
    i = max(inorder, start, end)
    # Pick the maximum value and make it root
    root = NewNode(inorder[i])
    # If this is the only element in
    # inorder[start..end], then return it
    if start == end:
        return root

    root.left = buildtree(inorder, start, i - 1)
    root.right = buildtree(inorder, i + 1, end)

    return root


def max(arr, strt, end):
    i, max = 0, arr[strt]
    maxind = strt
    for i in range(strt + 1, end + 1):
        if arr[i] > max:
            max = arr[i]
            maxind = i
    return maxind


def printinorder(node):
    if node is None:
        return

    printinorder(node.left)
    print(node.data, end=" ")
    printinorder(node.right)


inorder = fileopen()
Len = len(inorder)
root = buildtree(inorder, 0, Len - 1)
print("Tree is successfully built using inorder input file")
