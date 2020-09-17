mkdir Q2
cd Q2
git init 
touch 11940010.txt
echo "iitbhilai">>11940010.txt
cp 11940010.txt 11940230.txt
cp 11940010.txt 11941140.txt
mkdir Aayush
mkdir Santaz
mkdir Shubham
mv 11940010.txt Aayush
mv 11940230.txt Santaz
mv 11941140.txt Shubham
git add Aayush
git commit -m "commit 1"
git graph
git add Santaz
git commit -m "commit 2"
git graph
git add Shubham
git commit -m "commit 3"
git graph