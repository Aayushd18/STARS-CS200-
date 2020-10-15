 mkdir a2q3b 
 cd a2q3b
 echo " making of file1 " > file1
 echo " making of file2 " > file2
 git init
 git add file1
 git add file2
 git commit -m " commit1 "
 git branch branch1
 echo " add this to file1 " >> file1
 git add file1
 git commit -m " commit2 "
 git checkout branch1
 echo " add this to file2 " >> file2
 git add file2
 git commit -m " commit3 "
 git checkout master
 git graph
 git merge branch1
 git graph