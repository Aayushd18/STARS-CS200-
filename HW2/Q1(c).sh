git init Q1
cd Q1
touch first.txt
echo "hello">>first.txt
git add --patch first.txt
echo "google">>first.txt
git add -N first.txt
git add --patch first.txt
git graph