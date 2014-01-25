#!/bin/bash
PROJECT_HOME="/home/mz342/Project"
data=${PROJECT_HOME}/googlebooks-eng-all-2gram-20120701-de
targetWord="dear"
lstDir=${PROJECT_HOME}/list

for f in ${PROJECT_HOME}/google_books/*
do
    #if [${f} == *.txt]
    #then
	echo ${f}
    #fi
done
#python gramExtractor.py ${data} ${targetWord}

# while read line
# do
#     str=( $line )
#     if [ ${str[0]} == ${targetWord}* ] 
# 	then
# 	echo $line
#     fi
# done < ${data}