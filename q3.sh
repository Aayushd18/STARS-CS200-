#!/bin/sh

tmpfile=$(mktemp)
{
set -e

cd "$(git rev-parse --git-dir)"

# Find all the objects that are in packs:

find objects/pack -name 'pack-*.idx' | while read p ; do git show-index < $p | cut -f 2 -d ' ' 
done

# And now find all loose objects:

find objects/ \
    | egrep '[0-9a-f]{38}'\
    | grep -v /pack/ \
    | perl -pe 's:^.*([0-9a-f][0-9a-f])/([0-9a-f]{38}):\1\2:' \
;
} > ${tmpfile}

cat ${tmpfile} > file.txt


while IFS= read -r line; do
   echo "Hash value of the associated object: $line" ; 
   echo "Size of the object is:" $(git cat-file -s $line);
   echo "Type of object is:" $(git cat-file -t $line );
   echo "Contents of the object is:" $(git cat-file -p $line);
   echo "Exiting after completion of the process" $(git cat-file -e $line)
done < file.txt
read
