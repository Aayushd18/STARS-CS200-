#! /bin/bash

initialise(){
git init
echo "This Project creates a Familt tree using Git commands"
echo
echo "Please enter the name of head of the family"
read head
git checkout -b $head
git commit --allow-empty -m "head of the family"
return 1
}