"""
Gabriel Aptekar
The helper functions in order to make some test cases.

"""
from binarytree import convert, pprint, Node
import sys

#some helper functions that are called
def preorder_helper(node,answer):
    answer.append(node.value)
    if(node.left):
        preorder_helper(node.left,answer)
    if(node.right):
        preorder_helper(node.right,answer)
def inorder_helper(node,answer):
    if(node.left):
        inorder_helper(node.left,answer)
    answer.append(node.value)
    if(node.right):
        inorder_helper(node.right,answer)
def postorder_helper(node,answer):
    if(node.left):
        postorder_helper(node.left,answer)
    if(node.right):
        postorder_helper(node.right,answer)
    answer.append(node.value)

def preorder(node):
    "Returns a list with the preorder traversal of a tree"
    answer=[]
    preorder_helper(node,answer)
    return answer

def inorder(node):
    "Returns a list with the inorder traversal of a tree"
    answer=[]
    inorder_helper(node,answer)
    return answer

def postorder(node):
    "Returns a list with the preorder traversal of a tree"
    answer=[]
    postorder_helper(node,answer)
    return answer

def create_test_files(preorder,inorder,postorder,id=1):
    "Puts a test in each folder"
    with open("preorder/"+str(id)+".txt","w") as file:
        file.write(' '.join([str(x) for x in preorder]))
    with open("inorder/"+str(id)+".txt","w") as file:
        file.write(' '.join([str(x) for x in inorder]))
    with open("postorder/"+str(id)+".txt","w") as file:
        file.write(' '.join([str(x) for x in postorder]))


def balanced_test_case(lst,id=1):
    "Creates a balanced tree"
    tree= convert(lst)
    create_test_files(preorder(tree),inorder(tree),postorder(tree),"balanced_"+str(id))


def unbalanced_test_case(lst,id=1):
    "Creates an unbalanced tree from a list"
    tree=Node(lst[0])
    node=tree
    for val in lst[1:]:
        node.left=Node(val)
        node=node.left
    create_test_files(preorder(tree),inorder(tree),postorder(tree),"unbalanced_"+str(id))

def V_test_case(lst,id=1):
    "Creates a tree that looks like a V"
    tree=Node(lst[0])
    node=tree
    for val in lst[1:len(lst)//2]:
        node.left=Node(val)
        node=node.left
    node=tree
    for val in lst[len(lst)//2:]:
        node.right=Node(val)
        node=node.right
    create_test_files(preorder(tree),inorder(tree),postorder(tree),"V_"+str(id))
