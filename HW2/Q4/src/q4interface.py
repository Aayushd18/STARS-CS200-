import Q4
import preorder
import postorder
import zigzag


def exit():
    return 0


tree = Q4.fileopen()
Len = len(tree)
root = Q4.buildtree(tree, 0, Len - 1)
x = 1

while x != 0:
    print("\nThe Options of Traversals are :\n 1. Preorder\n 2. Postorder\n 3. ZigZag\n 4. Exit\n Enter the option number "
          "you want to use : ")
    choice = int(input())

    if choice == 1:
        x = preorder.preorder(root)

    if choice == 2:
        x = postorder.postorder(root)

    if choice == 3:
        x = zigzag.zizagtraversal(root)

    if choice == 4:
        x = exit()