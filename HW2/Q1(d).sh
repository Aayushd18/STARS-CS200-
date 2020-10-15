#! /bin/bash

#Initialise the Git Repository
git init mergecommits   
cd mergecommits 
# Making 5 different files and committing them individually
echo f1 > 1.txt 
echo f2 > 2.txt
echo f3 > 3.txt
echo f4 > 4.txt
echo f5 > 5.txt
git add 1.txt
git commit -m "1"
git add 2.txt
git commit -m "2"
git add 3.txt
git commit -m "3"
git add 4.txt
git commit -m "4"
git add 5.txt
git commit -m "5" 
#Checking the current state of the repo and obtaining the graph
git log 
git graph 

#This rebase will help bring the last 2 commits(4 and 5)
git rebase --interactive HEAD~2
# We are in the interactive session
# Replace the pick of commit 4 with squash 
# Exit the interactive console 
#Esc + :wq (twice)
# We are done
# check the log again merged commits
git log
git graph 
#done