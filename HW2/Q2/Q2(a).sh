mkdir q2a
cd q2a
git init
A[0]='11940010'
A[1]='11940230'
A[2]='11941140'
A[3]='master'
git init
echo 'dummy'>A
git add A
git commit -m"dummycommit"
echo 'dummy'>A
git add A
git commit --allow-empty -m"dummycommit"
git branch ${A[0]}
git branch ${A[1]}
git branch ${A[2]}
echo "Commiting randomly in different branches,this will take some time"
for((i=0;i<20;i++)); do
 sleep 1.2s
 ind=$(($RANDOM%4))
 git checkout ${A[$ind]}
 git add A
 git commit --allow-empty -m"A is added"
done
git graph --nodes clhrsagu