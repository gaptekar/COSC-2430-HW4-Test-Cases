"""
Created on Thu Apr  6 11:30:37 2017

@author: Gabriel
"""
from binarytree import convert, pprint, Node
import sys
sys.setrecursionlimit(1010)
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
    answer=[]
    preorder_helper(node,answer)
    return answer
def inorder(node):
    answer=[]
    inorder_helper(node,answer)
    return answer
def postorder(node):
    answer=[]
    postorder_helper(node,answer)
    return answer

def create_test_files(preorder,inorder,postorder,id=1):
    with open("preorder/"+str(id)+".txt","w") as file:
        file.write(' '.join([str(x) for x in preorder]))
    with open("inorder/"+str(id)+".txt","w") as file:
        file.write(' '.join([str(x) for x in inorder]))
    with open("postorder/"+str(id)+".txt","w") as file:
        file.write(' '.join([str(x) for x in postorder]))
                

def balanced_test_case(lst,id=1):
    
    #http://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-whilst-preserving-order
    #ensures uniqueness
    #seen = set()
    #seen_add = seen.add
    #lst=[x for x in lst if not (x in seen or seen_add(x))]
    tree= convert(lst)
    create_test_files(preorder(tree),inorder(tree),postorder(tree),"balanced_"+str(id))


def unbalanced_test_case(lst,id=1):
    tree=Node(lst[0])
    node=tree
    for val in lst[1:]:
        node.left=Node(val)
        node=node.left
    create_test_files(preorder(tree),inorder(tree),postorder(tree),"unbalanced_"+str(id))     
        
def V_test_case(lst,id=1):
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        