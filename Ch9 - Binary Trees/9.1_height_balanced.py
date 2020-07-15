class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insertLeft(self, newData):
        self.left = BinaryTree(newData)

    def insertRight(self, newData):
        self.right = BinaryTree(newData)

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def preorder(self):
        print(self.data, end='')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end='')
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end='')


def height(node):
    if node is None:
        return 0
    # else:
    #     # compute depth of each subtree
    #     lDepth = maxDepth(node.getLeft())
    #     rDepth = maxDepth(node.getRight())

    #     if lDepth > rDepth:
    #         print(lDepth + 1)
    #         return lDepth + 1
    #     else:
    #         print(rDepth + 1)
    #         return rDepth + 1
    return max(height(node.getLeft()), height(node.getRight())) + 1


def isBalanced(node):
    # base condition
    if node is None:
        return True

    # getting the height of left and right subtree
    lheight = height(node.getLeft())
    rheight = height(node.getRight())

    # allowed values for (lh - rh) are 1, -1, 0
    if(abs(lheight - rheight) <= 1 and isBalanced(node.getLeft()) == True and isBalanced(node.getRight()) == True):
        return True

    # if we reach here means tree is not height-balanced
    return False


# True case
treeRoot = BinaryTree(1)

treeRoot.insertLeft(2)
treeRoot.getLeft().insertLeft(3)
treeRoot.getLeft().insertRight(4)
treeRoot.getLeft().getRight().insertRight(5)

treeRoot.insertRight(5)

print(isBalanced(treeRoot))


# False case
# treeRoot = BinaryTree(1)
#
# treeRoot.insertLeft(2)
# treeRoot.getLeft().insertLeft(3)
# treeRoot.getLeft().insertRight(4)
# treeRoot.getLeft().getRight().insertRight(5)
#
# treeRoot.insertRight(6)
