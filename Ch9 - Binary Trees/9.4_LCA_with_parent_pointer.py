# Solution 1: does not work for all cases
#
# class BinaryTree:
#     def __init__(self, data):
#         self.data = data
#         self.right = None
#         self.left = None
#         self.parent = None
#
#     def insertLeft(self, newData):
#         self.left = BinaryTree(newData)
#         self.left.parent = self
#
#     def insertRight(self, newData):
#         self.right = BinaryTree(newData)
#         self.right.parent = self
#
#     def getLeft(self):
#         return self.left
#
#     def getRight(self):
#         return self.right
#
#     def getData(self):
#         return self.data
#
#     def getParent(self):
#         return self.parent
#
#     def setData(self, newData):
#         self.data = newData
#
#
# # left - root - right
# def returnInorder(node, nodeData1, nodeData2):
#     inorderList = []
#     result = []
#
#     def inorder(node):
#         if node:
#             inorder(node.getLeft())
#             # print(node.getData())
#             inorderList.append(node.getData())
#             if(node.getData() == nodeData1):
#                 result.append(node)
#                 # result.append(node.getData())
#             if(node.getData() == nodeData2):
#                 result.append(node)
#                 # result.append(node.getData())
#             inorder(node.getRight())
#
#
#     if len(inorderList) == 0:
#         # to take care of leaf case
#         if node:
#             if node.getLeft() or node.getRight():
#                 inorder(node)
#             else:
#                 inorderList.append(node.getData())
#
#     result.append(inorderList)
#
#     return result
#
#
# def LCA(root, node1, node2):
#     res = returnInorder(root, node1, node2)
#
#     nodeObj1 = res[0]
#     nodeObj2 = res[1]
#     inorderList = res[2]
#
#     # target nodes list
#     i1 = inorderList.index(node1)
#     i2 = inorderList.index(node2)
#
#     if i1 < i2:
#         targetList = inorderList[i1+1:i2]
#     else:
#         targetList = inorderList[i2+1:i1]
#
#
#     def helper(nodeObj1, nodeObj2, targetList):
#
#         parent1 = nodeObj1.getParent()
#         parent2 = nodeObj2.getParent()
#
#         # base case
#         if(parent1.getData() == parent2.getData()):
#             return parent1.getData()
#
#         # for node1, when not in targetList parent1 is the likely LCA
#         while parent1.getData() in targetList and parent1.getParent().getData() in targetList:
#             return helper(parent1, nodeObj2, targetList)
#
#         # for node2
#         while parent2.getData() in targetList and parent2.getParent().getData() in targetList:
#             return helper(nodeObj1, parent2, targetList)
#
#         return 'Something bad'
#
#
#     return helper(nodeObj1, nodeObj2, targetList)
#
#
#
# # Small tree
# treeRoot = BinaryTree('1')
#
# treeRoot.insertLeft('2')
# treeRoot.getLeft().insertLeft('3')
# treeRoot.getLeft().insertRight('4')
# treeRoot.getLeft().getRight().insertLeft('9')
# treeRoot.getLeft().getRight().insertRight('5')
#
# treeRoot.insertRight('6')
#
# print(LCA(treeRoot, '3', '5'))

# Find the LCA of node 3 and node 5 = 2

# print(LCA(treeRoot, '2', '4'))


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



# Solution 2:

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None

    def insertLeft(self, newData):
        self.left = BinaryTree(newData)
        self.left.parent = self

    def insertRight(self, newData):
        self.right = BinaryTree(newData)
        self.right.parent = self

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getData(self):
        return self.data

    def getParent(self):
        return self.parent

    def setData(self, newData):
        self.data = newData


# left - root - right
def returnInorder(node, nodeData1, nodeData2):
    inorderList = []
    result = []

    def inorder(node):
        if node:
            inorder(node.getLeft())
            # print(node.getData())
            inorderList.append(node.getData())
            if(node.getData() == nodeData1):
                result.append(node)
                # result.append(node.getData())
            if(node.getData() == nodeData2):
                result.append(node)
                # result.append(node.getData())
            inorder(node.getRight())


    if len(inorderList) == 0:
        # to take care of leaf case
        if node:
            if node.getLeft() or node.getRight():
                inorder(node)
            else:
                inorderList.append(node.getData())

    result.append(inorderList)

    return result


def LCA(root, node1, node2):
    res = returnInorder(root, node1, node2)

    nodeObj1 = res[0]
    nodeObj2 = res[1]
    inorderList = res[2]

    nodePath1 = []

    # Search path for node 1
    node1 = nodeObj1
    while node1 != None:
        nodePath1.append(node1.getData())
        node1 = node1.getParent()

    # search path for node 2
    node2 = nodeObj2
    while node2 != None:
        if node2.getData() in nodePath1:
            return node2.getData()
        node2 = node2.getParent()



# Small tree
treeRoot = BinaryTree('1')

treeRoot.insertLeft('2')
treeRoot.getLeft().insertLeft('3')
treeRoot.getLeft().insertRight('4')
treeRoot.getLeft().getRight().insertLeft('9')
treeRoot.getLeft().getRight().insertRight('5')

treeRoot.insertRight('6')

# print(treeRoot.getLeft().getLeft().getParent().getData())

print(LCA(treeRoot, '5', '6'))

# Find the LCA of node 3 and node 5 = 2

# print(LCA(treeRoot, '2', '4'))


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
