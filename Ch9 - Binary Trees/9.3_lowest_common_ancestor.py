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


# left - root - right
def returnInorder(node):
    inorderList = []

    def inorder(node):
        if node:
            inorder(node.getLeft())
            # print(node.getData())
            inorderList.append(node.getData())
            inorder(node.getRight())


    if len(inorderList) == 0:
        # to take care of leaf case
        if node:
            if node.getLeft() or node.getRight():
                inorder(node)
            else:
                inorderList.append(node.getData())

    return inorderList



def LCA(root, node1, node2):

    leftSubtree = returnInorder(root.getLeft())
    rightSubtree = returnInorder(root.getRight())

    if((node1 in leftSubtree and node2 in rightSubtree) or (node1 in rightSubtree and node2 in leftSubtree)):
        return root.getData()

    elif(node1 in leftSubtree and node2 in leftSubtree):
        return LCA(root.getLeft(), node1, node2)

    elif(node1 in rightSubtree and node2 in rightSubtree):
        return LCA(root.getRight(), node1, node2)

    # this means the nodes are in one subtree and are related
    elif(node1 == root.getData()):
        return root.getData()

    elif(node2 == root.getData()):
        return root.getData()

    return "Nodes are not found"


# Small tree
treeRoot = BinaryTree('1')

treeRoot.insertLeft('2')
treeRoot.getLeft().insertLeft('3')
treeRoot.getLeft().insertRight('4')
treeRoot.getLeft().getRight().insertLeft('9')
treeRoot.getLeft().getRight().insertRight('5')

treeRoot.insertRight('6')

# Find the LCA of node 3 and node 5 = 2

print(LCA(treeRoot, '2', '4'))


# bigger tree
# treeRoot = BinaryTree(314)

# treeRoot.insertLeft(6)
# treeRoot.getLeft().insertRight(2)
# treeRoot.getLeft().getRight().insertRight(3)
# treeRoot.getLeft().insertLeft(4)
# treeRoot.getLeft().getLeft().insertLeft(5)

# treeRoot.insertRight(16)
# treeRoot.getRight().insertLeft(12)
# treeRoot.getRight().getLeft().insertLeft(13)
# treeRoot.getRight().insertRight(14)
# treeRoot.getRight().getRight().insertRight(15)

# print(LCA(treeRoot, 5, 2))
