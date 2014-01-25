#!/bin/bash
PROJECT_HOME="/home/mz342/Project"
data=${PROJECT_HOME}/googlebooks-eng-all-2gram-20120701-de
targetWord="dear"
lstDir=${PROJECT_HOME}/list
outputDir=${PROJECT_HOME}/output/


	    data=${PROJECT_HOME}/0005.txt
	    while read targetWord
	    do
		python gramExtractor.py ${data} ${targetWord} ${outputDir}
	    done < "${lstDir}/word (copy).txt"	 