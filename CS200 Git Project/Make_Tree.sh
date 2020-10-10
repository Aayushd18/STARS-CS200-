#! /bin/bash

make_tree(){
while : 
do
echo "The Functions that you can use are as follows :- "
echo '1.) Add one child to a parent \n 2.) Add two children to a parent parent \n 3.) Add wife name \n 4.) Add husband name \n 5.) Exit and Get Git graph \n \n'
echo "Enter the number of function you want to use :- "
read num
case $num in [1]) add_one_child ;;
[2]) add_two_child ;;
[3]) add_wife_name ;;
[4]) add_husband_name ;;
[5]) exit_function ; break ;;
*) echo "invalid input" ;;
esac;
done
return 1
}