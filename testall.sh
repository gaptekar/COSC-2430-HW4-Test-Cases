#Created by Gabriel Aptekar
#this program will run your compiled  program against all test cases
#the names of the subfolders
RESPONSES=responses
DIFFERENCES=differences
timeout="10s"
# clean
rm -f *.out *.err *.stderr *.stdout *.diff 2>/dev/null
rm -f hw4
#Compile the code
g++ -std=c++11 *.cpp -o hw4 2>COMPILE.err
#will create folders so that you can see
#the results of the program
if [ ! -d $RESPONSES ]; then
    mkdir $RESPONSES
else
    rm -rf $RESPONSES/*
fi
if [ ! -d $DIFFERENCES ]; then
    mkdir $DIFFERENCES
else
    rm -rf $DIFFERENCES/*
fi

#run through all the test cases in the tests folder
#SAVEIFS=$IFS
#IFS=$(echo -en "\n\b")
for test in preorder/*
do
  #if the file is a test file
  if [ ${test: -4} == ".txt" ]; then
    #get the name of the text file and store it in filename
    filename=$(basename "$test")
    filename="${filename%.*}"
    #is there an answer for this test case
    if [ -e inorder/$filename.txt ]; then
      if [ -e postorder/$filename.txt ]; then
        #store the program output in the response folder
        timeout -k $timeout $timeout ./hw4 "preorder=preorder/${filename}.txt;inorder=inorder/${filename}.txt" 1>$RESPONSES/$filename.stdcout
        # compare the input and output, output the difference to 1.diff
        diff -iEBwu $RESPONSES/$filename.stdcout postorder/$filename.txt > $DIFFERENCES/$filename.diff
        # if diff returns nothing, it means you pass the test case (Your output file is correct)
        if [ $? -ne 0 ]; then
            # display "test case FAILED" to the screen. The word "FAILED" is highlighted in Red color
            echo -e "Test case: "$filename"    \033[1;91mFAILED.\033[0m"
        else
            # display "test case PASSED" to the screen. The word "PASSED" is highlighted in Green color
            echo -e "Test case: "$filename"    \033[1;92mPASSED.\033[0m"
            # remove the diff file
            rm -f $DIFFERENCES/$filename.diff
        fi
      fi
    fi
  fi
done
