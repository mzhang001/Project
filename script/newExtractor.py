import os, os.path
import io
import multiprocessing
import re
#def process_piece(outputDir,wordLst,filename,start,end):
def process_piece(outputDir,wordLst,filename):
	#wordLst = ['computer','dear']	
	f = open(filename,'r')
	basename = os.path.basename(filename)
	out_f = open(outputDir + '/' + word  + '/' + basename, 'w')
	#print end
	'''
	for word in wordLst:
		#if(end is not None):
		out_f = open(outputDir + '/' + word  + '/' + basename + '_' + str(start), 'w')
		#else:				
		#	out_f = open(outputDir + '/' + word  + '/' + basename + '_' + str(start), 'w')
		fLst[word] = out_f
	'''
	with open(filename,'r') as f:
		f.seek(start+1)
		if(end is None):
			text=f.read()
		else: 
			nbytes=end-start+1
			text=f.read(nbytes)
	
	i = 0
	flag = False
	buf = text.split("\n")
	for line in buf:
		line = line.lower()
		data = line.split("\t")
		words = data[0].split()
		for word in words:
			if word == wordsLst[i]:
				flag = True
				out_f.writelines(line + "\n")
			elif flag:
				i+=1
				if(i == len(wordLst)):
					break
				flag = False
		if(i == len(wordLst)):
			break
	
	out_f.close()	
	f.close()
	return 0	
    # process text here. creating some object to be returned
    # You could wrap text into a StringIO object if you want to be able to
    # read from it the way you would a file.


def extract_information(outputDir, wordLst, inputFileName, word):
	firstLetter = wordLst[0][0]	
	f = open(inputFileName,'r')
	#basename = os.path.basename(inputFileName)
	out_f = open(outputDir + '/' + word  + '/' + firstLetter, 'w')
	
	text=f.read()
	i = 0
	flag = False
	buf = text.split("\n")

	wordSet = set(wordLst)
	for line in buf:
		line = line
		data = line.split("\t")
		word = data[0].lower()
		if word in wordSet:
			out_f.writelines(line + "\n")
	out_f.close()	
	f.close()
	return 0
	
def extract_information_inorder(outputDir,wordLst,inputFileName, word):
	firstLetter = wordLst[0][0]	
	f = open(inputFileName,'r')
	#basename = os.path.basename(inputFileName)
	out_f = open(outputDir + '/' + word  + '/' + firstLetter, 'w')
	
	text=f.read()
	i = 0
	flag = False
	buf = text.split("\n")
	for line in buf:
		line = line
		data = line.split("\t")
		word = data[0].lower()
		
		if word == wordLst[i]:
			flag = True
			out_f.writelines(line + "\n")
		elif flag:
			i += 1
			if(i == len(wordLst)):
				break
			if word == wordLst[i]:
				out_f.writelines(line + "\n")
			else: 
				flag = False
	out_f.close()	
	f.close()
	return 0

def wrapper(args):
    return process_piece(*args)

def newlinebefore(f,n):
    f.seek(n)
    c=f.read(1)
    while c!='\n' and n > 0:
        n-=1
        f.seek(n)
        c=f.read(1)

    f.seek(n)
    return n


#outputDir = '/home/mz342/Project/documentFrequency'
#wordLst = ["a","a."]
#inputFileName = '/home/mz342/Project/googlebooks-eng-all-1gram-20120701-a'
#targetWord = "mouse"

#extract_information_inorder(outputDir,wordLst,inputFileName,targetWord)


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

