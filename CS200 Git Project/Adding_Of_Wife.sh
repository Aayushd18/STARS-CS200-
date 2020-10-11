#! /bin/bash

add_wife_name() {
Echo "Which person's wife name you want to add:- "
read $person
git checkout $person
echo "Enter the name of wife :- "
read wife_name
git tag Wife=$wife_name
return 1
}