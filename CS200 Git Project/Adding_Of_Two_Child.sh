#! /bin/bash

add_two_child() {
echo "Which parent's children you want to add :- "
read parent
echo "Enter the name of first child := "
read child1
git checkout $parent
git checkout -b $child1
git commit --allow-empty -m "$child Welcome"
git checkout $parent
echo "Enter the name of second child :- "
read child2
git checkout -b $child2
git commit --allow-empty -m "$child2 Welcome"
return 1
}