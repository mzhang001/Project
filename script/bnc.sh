HOME_PATH=/home/mz342/github/lexical/src
PROJECT_PATH=/home/mz342/Project
OUT_DIR=${PROJECT_PATH}/output/bnc

while read word
do
    java -classpath ${HOME_PATH} ExecuteMe ${word} > ${OUT_DIR}/${word}.txt
done < ${PROJECT_PATH}/list/word.txt