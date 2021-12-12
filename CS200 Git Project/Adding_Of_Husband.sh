#! /bin/bash

add_husband_name() {
echo "Which person's husbands name you want to add :- "
read person
git checkout $person
echo "Enter the name of husband :- "
read husband_name
git tag Husband=$husband_name
return 1
}