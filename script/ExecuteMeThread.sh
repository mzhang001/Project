#!/bin/bash
PROJECT_HOME="/home/mz342/Project"
#data=${PROJECT_HOME}/googlebooks-eng-all-2gram-20120701-de
targetWord="dear"
lstDir=${PROJECT_HOME}/list
outputDir=${PROJECT_HOME}/output/

while read gramFolder;
do
    for file in ${gramFolder}/*
    do
	echo $file
	IFS='/' read -a pathTokens <<< ${file};
	IFS=' ' read -a pathTokens <<< ${pathTokens[0]};
	fileName=${pathTokens[5]}
	gramName=${pathTokens[4]}
	if [[ $fileName != *.1 ]] 
	then 
	    cp ${file} ${PROJECT_HOME}/${fileName}
	    gunzip ${PROJECT_HOME}/${fileName}
	    echo ${PROJECT_HOME}/${fileName}
	   
	    IFS='.' read -a data <<< ${fileName};
	    IFS=' ' read -a data <<< ${data[0]};
	    data=${PROJECT_HOME}/${data[0]}
	    echo ${gramName}

	    python gramExtractorThread.py ${data} ${outputDir}/${gramName}/
		
	    rm ${data}
	    rm ${PROJECT_HOME}/${fileName}
	    #rm 
	fi
	#mv ${file} ${PROJECT_HOME}
	#rm 
    done
done < ${lstDir}/gramThreadList.txt

# for f in ${PROJECT_HOME}/google_books
# do
    
# done
# 

# while read line
# do
#     str=( $line )
#     if [ ${str[0]} == ${targetWord}* ] 
# 	then
# 	echo $line
#     fi
# done < ${data}