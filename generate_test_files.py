"""
Gabriel Aptekar
Creates the test cases using the functions I created in the other file
"""
from tree_tools import V_test_case,balanced_test_case,unbalanced_test_case
import sys
sys.setrecursionlimit(1100) #python isn't really designed for this


#create the test cases
cases=[2,5,10,20,50,100,200,500,1000]
for case in cases:
    args=[list(range(case)), case]
    balanced_test_case   (*args)
    unbalanced_test_case (*args)
    V_test_case          (*args)
