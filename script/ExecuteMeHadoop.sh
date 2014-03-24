#!/bin/bash
PROJECT_HOME="/home/mz342/Project"
#data=${PROJECT_HOME}/googlebooks-eng-all-2gram-20120701-de
targetWord="dear"
lstDir=${PROJECT_HOME}/list
outputDir=${PROJECT_HOME}/hadoopOutput
inputDir=${PROJECT_HOME}/data/input
#python createFolder.py ${outputDir} ${lstDir}/5gram_dep.txt 

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
	    IFS='.' read -a data <<< ${fileName};
	    IFS=' ' read -a data <<< ${data[0]};
	    data=${data[0]}

	    gunzip -c ${file} > ${inputDir}/${data}
            #cp ${file} ${PROJECT_HOME}/${fileName}
	    #gunzip ${PROJECT_HOME}/${fileName}
	    echo ${inputDir}/${data}
            #data=${PROJECT_HOME}/${data[0]}
	    echo ${gramName}

	    java -jar hadoop.jar ${inputDir} ${outputDir}/${gramName} ${data}
            #python gramExtractorThread.py ${data} ${outputDir}/${gramName}/	
	    rm ${inputDir}/${data}
	    #rm ${PROJECT_HOME}/${fileName}
	    #rm 
	fi
	#mv ${file} ${PROJECT_HOME}
	#rm 
    done
done < ${lstDir}/5gram_dep.txt

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
# done < ${data}From mz342 Thu Feb 13 13:56:52 2014
Date: Thu, 13 Feb 2014 13:56:52 +0000
To: zhangmeng1010@gmail.com Document .txt
Subject: Hello World
User-Agent: Heirloom mailx 12.5 6/20/10
MIME-Version: 1.0
Content-Type: multipart/mixed;
 boundary="=_52fccf24.V7vWVnKPnEiSBSzlUsRin6k9XmeZ3J6KVWN7t1Q2TUGsDs6/"

This is a multi-part message in MIME format.

--=_52fccf24.V7vWVnKPnEiSBSzlUsRin6k9XmeZ3J6KVWN7t1Q2TUGsDs6/
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
Content-Disposition: inline








--=_52fccf24.V7vWVnKPnEiSBSzlUsRin6k9XmeZ3J6KVWN7t1Q2TUGsDs6/
Content-Type: application/x-sh
Content-Transfer-Encoding: base64
Content-Disposition: attachment;
 filename="bnc.sh"

SE9NRV9QQVRIPS9ob21lL216MzQyL2dpdGh1Yi9sZXhpY2FsL2JpbgpQUk9KRUNUX1BBVEg9
L2hvbWUvbXozNDIvUHJvamVjdApPVVRfRElSPSR7UFJPSkVDVF9QQVRIfS9vdXRwdXQvYm5j
X3dpdGhvdXRUYXJnZXQKCndoaWxlIHJlYWQgd29yZApkbwogICAgamF2YSAtY2xhc3NwYXRo
ICR7SE9NRV9QQVRIfSBFeGVjdXRlTWUgJHt3b3JkfSA+ICR7T1VUX0RJUn0vJHt3b3JkfS50
eHQKZG9uZSA8ICR7UFJPSkVDVF9QQVRIfS9saXN0L3dvcmQudHh0

--=_52fccf24.V7vWVnKPnEiSBSzlUsRin6k9XmeZ3J6KVWN7t1Q2TUGsDs6/--

