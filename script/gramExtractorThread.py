import sys
import re
import threading
import time
import io
import os, os.path
import multiprocessing
from multiprocessor import process_piece, wrapper, newlinebefore
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

def returnList(listPath):
	wordLst = []
	with io.open(listPath, 'r') as file:
		for word in file:
			word = word.rstrip()
			wordLst.append(word)
	return wordLst

def returnGramFolderName(gramLst):
	names = []
	for path in gramLst:
		tokens = path.split('/')
		names.append(tokens[5])
	return names
		
def createFolder(outputDir, gramFolderNames, wordLst):
	for gram in gramFolderNames:
		gramDir = outputDir + '/' + gram
		if not os.path.exists(gramDir):
    			os.makedirs(gramDir)	
		for word in wordLst:
			wordDir = gramDir + '/' + word
			if not os.path.exists(wordDir):
    				os.makedirs(wordDir)
def printList(lst):
	for word in lst:
		print word

wordLst = returnList(lstDir + 'wordThread.txt')
printList(wordLst)
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



#def process_piece(outputDir,wordLst,filename,start,end):

args=zip(outputDir_re, wordLst_re, filename_re, start_byte, end_byte)
#for arg in args:
#	print arg
#print args
pool=multiprocessing.Pool(12)
result=pool.map(wrapper,args)


