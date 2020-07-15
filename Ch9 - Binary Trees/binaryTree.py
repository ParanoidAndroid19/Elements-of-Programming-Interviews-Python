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


treeRoot = BinaryTree(1)

treeRoot.insertLeft(2)
treeRoot.getLeft().insertLeft(3)
treeRoot.getLeft().insertRight(4)
treeRoot.getLeft().getRight().insertRight(5)

treeRoot.insertRight(6)

treeRoot.preorder()
print()
treeRoot.inorder()
print()
treeRoot.postorder()
