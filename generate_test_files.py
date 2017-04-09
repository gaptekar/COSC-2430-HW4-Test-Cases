from tree_tools import V_test_case,balanced_test_case,unbalanced_test_case
import sys
sys.setrecursionlimit(1100)


for i in [2,5,10,20,50,100,200,500,1000]:
    balanced_test_case( list(range(1,i+1)),i)
for i in [2,5,10,20,50,100,200,500,1000]:
    unbalanced_test_case( list(range(1,i+1)),i)    
for i in [2,5,10,20,50,100,200,500,1000]:
    V_test_case( list(range(1,i+1)),i)