#!/bin/bash

CHOSEN_NUMBER=$1
NAME=$2

echo "$NAME, you picked \"$CHOSEN_NUMBER\" as your answer..."
if [ $CHOSEN_NUMBER == "0" ]
then
	echo "Hmm... You were too lazy to choose a bigger number, so just get out!"
	exit
fi

echo "Now count $CHOSEN_NUMBER seconds..."
echo

for ((i=0; i<$CHOSEN_NUMBER; i++))
do
	sleep 1
	count=$(( $i + 1 ))
	echo "Counting $count..."
done

echo
echo "You just wasted $CHOSEN_NUMBER seconds! :P"
