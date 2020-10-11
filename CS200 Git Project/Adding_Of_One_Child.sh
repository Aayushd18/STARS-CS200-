#! /bin/bash

add_one_child() {
echo "Enter the name of the person to be added :- "
read new 
echo "On which parent you want to add $new :- "
read parent
git checkout $head
git checkout -b $new
git commit --allow-empty -m "$new Welcome"
return 1
}