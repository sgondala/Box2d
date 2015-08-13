#!/bin/bash

PROJECT_ROOT=../
EXE=$PROJECT_ROOT/mybins/cs296_06_exe
DATA=$PROJECT_ROOT/data
CSVI=$DATA/g06_lab05data_02.csv
CSVO=$DATA/g06_lab05data_random.csv

rm -f $CSVO
touch $CSVO

mkdir -p $DATA

for a in {1..40}
do
 i=$(awk -v var=$RANDOM 'BEGIN{srand(var); total=10; max=20; count=0;
	while(count < total) { 
		rnd=int(rand() * max); 
		if (array[rnd] == 0) { 
			count++; 
			array[rnd]++; 
		}
	}
	for(i=1; i<=max; i++) {
		if(array[i]) 
                print i;}}')
 i=($i)
 let "s = ($a - 1) * 20 + 1"
 let "e = $a * 20"
 old_IFS=$IFS
 IFS=$'\n'
 lines=($(sed -n "$s,$e"'p' $CSVI|cat)) # array
 IFS=$old_IFS
 for b in {0..10}
 do
  temp="${i[$b]}"
  echo "${lines[temp]}" >> $CSVO
 done
done 

exit 0
