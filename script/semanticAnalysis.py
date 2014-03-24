import math
import extractor
from customMath import get_cosine, tfidf
import operator
import newExtractor
import os

startYear = 1800
endYear = 2000
space = 5
targetWord = "mouse"

intervals = (endYear - startYear) / space + 1

def yearToIndex(year):
	return (year - startYear) / space

def indexToYear(index):
	return index * space + startYear

def print_words(dictmap):
	i = 0
	for stat in dictmap:
		year = indexToYear(i)
		i += 1		
		for word in stat:
			print year,' ',word,' ',stat[word]

def groupMapByStartLetter(dictmap):
	mapByLetter = {}
	for i in range(intervals):
		year = indexToYear(i)
		for word in dictmap[i]:
			count = dictmap[i][word]
			if word not in mapByLetter:
				mapByLetter[word] = {}
				mapByLetter[word][year] = count
			else:
				if year not in mapByLetter:
					mapByLetter[word][year] = count
				else:
					mapByLetter[word][year] += count
	return mapByLetter 
		

def getCounts(dictmap):
	counts = {}
	for index in dictmap:
		words = list(index.keys())
		for word in words:
			if word not in counts:
				counts[word] = index[word]
			else:
				counts[word] += index[word]
	return counts

def splitmap(mapByLetter):
	lstGroupLetter = []
	lstGroupLetter.append(set())	
	letters = returnAllLetters()
	letter_i = 0
	word_i = 0
	keys = sorted(list(mapByLetter.keys()))
	while word_i < len(mapByLetter.keys()):
		print keys[word_i]
		startLetter = keys[word_i][0]
		if letter_i == 26: break		
		if not startLetter.isalpha(): 
			word_i += 1			
			continue
		elif not startLetter == letters[letter_i]:
			letter_i += 1
			lstGroupLetter.append(set())
		else:
			if keys[word_i] not in lstGroupLetter[letter_i]:
				lstGroupLetter[letter_i].add(keys[word_i])
			word_i += 1
	return lstGroupLetter

		
		

def returnAllLetters():
	letters = []
	begin='a'
	end='z'
    	beginNum = ord(begin)
	endNum = ord(end)
	for number in range(beginNum, endNum+1):
		letters.append(chr(number))
	return letters








[dictmap,dfmap] = extractor.getMap(targetWord,startYear,endYear,space)
#print_words(dictmap)
mapByLetter = groupMapByStartLetter(dictmap)



dfmapByLetter = groupMapByStartLetter(dfmap)
counts = getCounts(dictmap)



homepath = "/home/mz342/Project/"
dataprefix = "/home/mz342/Project/google_books/1gram/googlebooks-eng-all-1gram-20120701-"
outputDir = homepath + "documentFrequency/"

letters = returnAllLetters()
lstGroupLetter = splitmap(mapByLetter)


for i in range(26):
	zipName = dataprefix + letters[i] + ".gz"
	fileName = "googlebooks-eng-all-1gram-20120701-" + letters[i]
	    #gunzip ${PROJECT_HOME}/${fileName}
	os.system("cp " + zipName + " " + homepath + fileName + ".gz")
	os.system("gunzip " + homepath + fileName + ".gz")

	newExtractor.extract_information(outputDir, list(lstGroupLetter[i]),homepath + fileName, "mouse")

	os.system("rm " + homepath + fileName + ".gz")
	os.system("rm " + homepath + fileName)



'''
tfidfmap = tfidf(dictmap,dfmap)



words = sorted(list(mapByLetter.keys()))


for word in words:
	startLetter = word[0]
	if startLetter.isalpha():
		years = sorted(list(mapByLetter[word]))
		for year in years:
			print word,' ',year,' ',dfmapByLetter[word][year]

def readVector(fileName, startYear=1800, endYear=2000, yearSpace=10):
	f = open(fileName,'r')
	for line in f:
		line = line.rstrip()
		[word,year,count] = line.split("\t")
		
readVector("mouseDF.txt")


countsFiltered = dict(sorted(counts.iteritems(), key=operator.itemgetter(1), reverse=True)[100:])

for i in range(intervals):
	for key in list(countsFiltered.keys()):
		if key in dictmap[i]:
			dictmap[i].pop(key, None)
			


#for i in range(intervals - 1):
#	year = indexToYear(i)

for i in range(intervals - 1):
	year = indexToYear(i)
	print year," ",indexToYear(i+1)," ",get_cosine(dictmap[i],dictmap[i+1])
	#for j in range(i + 1,intervals):
"""
	#	print str(year), " ", str(indexToYear(j)), " ", get_cosine(dictmap[i],dictmap[j])	
	#for key in dictmap[i]:
	#	print year," ",key," ",dictmap[i][key]
'''
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

