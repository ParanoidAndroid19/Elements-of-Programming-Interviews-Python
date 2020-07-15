
# Solution 1:

# 2 traversals and 1 list comparison
# Time complexity = O(n) + O(n) + O(n) = O(n)
# O(n) + O(n) // traversals
# + O(n) // if same no. of items in the list
# + O(1) // otherwise

# Space Complexity = O(h)

preorderList = []
inorderList = []
postorderList = []
oppinorderList = []

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
        print(str(self.data)+', ', end='')
        preorderList.append(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(str(self.data)+', ', end='')
        inorderList.append(self.data)
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(str(self.data)+', ', end='')


    def oppinorder(self):
        if self.right:
            self.right.oppinorder()
        print(str(self.data)+', ', end='')
        oppinorderList.append(self.data)
        if self.left:
            self.left.oppinorder()



def isSymmetrical(tree):
    print('inorder: left - root - right')
    tree.getLeft().inorder()
    print()
    tree.getRight().oppinorder()
    print()
    if (inorderList == oppinorderList):
        print('The tree is symmetrical')
    else:
        print('The tree is not symmetrical')



# symmetric tree
# treeRoot = BinaryTree(314)

# treeRoot.insertLeft(6)
# treeRoot.getLeft().insertRight(2)
# treeRoot.getLeft().getRight().insertRight(3)
# treeRoot.getLeft().insertLeft(4)
# treeRoot.getLeft().getLeft().insertLeft(5)

# treeRoot.insertRight(6)
# treeRoot.getRight().insertLeft(2)
# treeRoot.getRight().getLeft().insertLeft(3)
# treeRoot.getRight().insertRight(4)
# treeRoot.getRight().getRight().insertRight(5)



# Asymmetrical due to data difference
# treeRoot = BinaryTree(314)

# treeRoot.insertLeft(6)
# treeRoot.getLeft().insertRight(2)
# treeRoot.getLeft().getRight().insertRight(13)
# treeRoot.getLeft().insertLeft(4)
# treeRoot.getLeft().getLeft().insertLeft(5)

# treeRoot.insertRight(6)
# treeRoot.getRight().insertLeft(2)
# treeRoot.getRight().getLeft().insertLeft(3)
# treeRoot.getRight().insertRight(4)
# treeRoot.getRight().getRight().insertRight(5)



# Asymmetrical due to structural difference
treeRoot = BinaryTree(314)

treeRoot.insertLeft(6)
treeRoot.getLeft().insertRight(2)
treeRoot.getLeft().getRight().insertRight(3)

treeRoot.insertRight(6)
treeRoot.getRight().insertLeft(2)

# Symmetric
# treeRoot.getRight().getLeft().insertLeft(3)

# Asymmetric
treeRoot.getRight().getLeft().insertRight(3)

isSymmetrical(treeRoot)


# Solution 2: According to EPI

# Time complexity = O(n)
# Space complexity = O(h)

# def isSymmetrical(tree):
#     def check_symmetry(leftSubtree, rightSubtree):
#         if not leftSubtree and not rightSubtree:
#             return True
#
#         elif leftSubtree and rightSubtree:
#             return (leftSubtree.getData() == rightSubtree.getData()
#             and check_symmetry(leftSubtree.getLeft(), rightSubtree.getRight())
#             and check_symmetry(leftSubtree.getRight(), rightSubtree.getLeft()))
#
#         # one subtree is empty and other one is not
#         return False
#
#     return not tree or check_symmetry(tree.getLeft(), tree.getRight())
