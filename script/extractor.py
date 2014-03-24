import math




def getMap(targetWord="mouse", startYear="1800", endYear="2000", yearSpace="1"):
	space = yearSpace
	intervals = (endYear - startYear) / space + 1

	def yearToIndex(year):
		return (year - startYear) / space

	def indexToYear(index):
		return index * space + startYear
	

	inputFile = "/home/mz342/Project/output/5gram/" + targetWord + ".txt"
	f = open(inputFile,'r')
	dictmap = []
	documentFreqMap = []
	for i in range(intervals):
		dictmap.append({})
		documentFreqMap.append({})
	for line in f:
		data,year,count_single,count_book = line.split("\t")
		year = int(year)
		count_single = int(count_single)
		count_book = int(count_book)
		if (year < startYear) or (year > endYear):
			continue
		index = yearToIndex(year)
		#print index

		mapAtIndex = dictmap[index]
		words = data.split(" ")
		for word in words:
			if word == targetWord:
				continue
			if(word not in mapAtIndex):
				(dictmap[index])[word] = count_single
				(documentFreqMap[index])[word] = count_book
			else:
				(dictmap[index])[word] += count_single
				(documentFreqMap[index])[word] += count_book
		#break
	f.close()
	return [dictmap,documentFreqMap]

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def print_words(dictmap):
	for stat in dictmap:
		for word in stat:
			print word,' ',stat[word]



#for i in range(intervals - 1):
#	year = indexToYear(i)
#	print year," ",indexToYear(i+1)," ",get_cosine(dictmap[i],dictmap[i+1])
	#for j in range(i + 1,intervals):
	#	print str(year), " ", str(indexToYear(j)), " ", get_cosine(dictmap[i],dictmap[j])	
	#for key in dictmap[i]:
	#	print year," ",key," ",dictmap[i][key]






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

