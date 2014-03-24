import sys
import re
import threading
import time
import io
import os, os.path
import multiprocessing
from customIO import returnWordSet, returnList, returnGramFolderName, createFolder, printList

from multiprocessor import process_piece, setWrapper,newlinebefore
# class myThread (threading.Thread):
# 	def __init__(self,fileName,target,outputDir):
# 		threading.Thread.__init__(self)
# 		self.fileName = fileName
# 		self.target = target
# 		self.outputDir = outputDir
# 	def run(self):
# 		f = open(fileName,"r")
# 		out_f = open(outputDir + targetWord + ".txt", "a")
# 		targetWord = targetWord
# 		line = f.readline()
# 		flag = False
# 		while line != "":
# 			line = line.lower()
# 			tokens = re.split(r'[ \t]', line)
# 			#print tokens[0]
# 			for i in range(len(tokens) - 1):
# 				if tokens[i] == targetWord:
# 					out_f.writelines(line)
# 					break

# 			line = f.readline()
# 		f.close()
# 		out_f.close()

filename = sys.argv[1]
outputDir = sys.argv[2]

#filename = "/home/mz342/Project/googlebooks-eng-all-5gram-20120701-zz"
#outputDir = "/home/mz342/Project/output/5gram"

homeFolder = "/home/mz342/Project"
lstDir = homeFolder + "/list/"
wordLst = returnList(lstDir + 'CCS_wordlist.txt')
wordSet = returnList(lstDir + 'CCS_wordlist.txt')

#printList(wordLst)
fsize=os.path.getsize(filename) #size of file (in bytes)

#break the file into 40 chunks for processing.
nchunks=36
initial_chunks=range(1,fsize,fsize/nchunks)

with open(filename,'r') as f:
	start_byte=sorted(set([newlinebefore(f,i) for i in initial_chunks]))

end_byte=[i-1 for i in start_byte] [1:] + [None]

filename_re=[filename]*len(start_byte)
outputDir_re = [outputDir]*len(start_byte)
wordLst_re = [wordLst]*len(start_byte)
wordSet_re = [wordSet]*len(start_byte)


#args=zip(outputDir_re, wordLst_re, filename_re, start_byte, end_byte)
#pool=multiprocessing.Pool(12)
#result=pool.map(wrapper,args)

args=zip(outputDir_re,wordSet_re, filename_re, start_byte,end_byte)
pool=multiprocessing.Pool(12)
result=pool.map(setWrapper,args)

From mz342 Thu Feb 13 13:56:52 2014
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

From mz342 Thu Feb 13 13:57:08 2014
Date: Thu, 13 Feb 2014 13:57:08 +0000
To: zhangmeng1010@gmail.com
Subject: Hello World
User-Agent: Heirloom mailx 12.5 6/20/10
MIME-Version: 1.0
Content-Type: multipart/mixed;
 boundary="=_52fccf34.nWRC9mmW9f0DO4c9Xsj+wnc9+AeX1wuZat0Aktl7LJw4Q8/L"

This is a multi-part message in MIME format.

--=_52fccf34.nWRC9mmW9f0DO4c9Xsj+wnc9+AeX1wuZat0Aktl7LJw4Q8/L
Content-Type: text/x-python;
 charset=us-ascii
Content-Transfer-Encoding: 7bit
Content-Disposition: attachment;
 filename="createFolder.py"

from customIO import createFolder, returnGramFolderName, returnList
import sys

outputDir = sys.argv[1]
gramPath = sys.argv[2]

homeFolder = "/home/mz342/Project"
lstDir = homeFolder + "/list/"
wordPath = lstDir + "CCS_wordlist.txt"

gramLst = returnList(gramPath)
wordLst = returnList(wordPath)
gramFolderNames = returnGramFolderName(gramLst)
createFolder(outputDir, gramFolderNames, wordLst)


From mz342 Thu Feb 13 13:56:52 2014
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


--=_52fccf34.nWRC9mmW9f0DO4c9Xsj+wnc9+AeX1wuZat0Aktl7LJw4Q8/L--

