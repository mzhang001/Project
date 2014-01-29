import os, os.path
import io
import multiprocessing
import re
#def process_piece(outputDir,wordLst,filename,start,end):
def process_piece(outputDir,wordLst,filename,start,end):
	#wordLst = ['computer','dear']	
	f = open(filename,'r')
	basename = os.path.basename(filename)
	fLst = {}
	#print end
	for word in wordLst:
		#if(end is not None):
		out_f = open(outputDir + '/' + word  + '/' + basename + '_' + str(start), 'w')
		#else:				
		#	out_f = open(outputDir + '/' + word  + '/' + basename + '_' + str(start), 'w')
		fLst[word] = out_f

	with open(filename,'r') as f:
		f.seek(start+1)
		if(end is None):
			text=f.read()
		else: 
			nbytes=end-start+1
			text=f.read(nbytes)
	
	buf = text.split("\n")
	for line in buf:
		line = line.lower()
		tokens = re.split(r'[ \t]', line)
		for i in range(len(tokens) - 1):
			for targetWord in wordLst:
				if tokens[i] == targetWord:
					fLst[targetWord].writelines(line + "\n")
	for key in fLst:
		fLst[key].close()	
	f.close()
	return 0	
    # process text here. creating some object to be returned
    # You could wrap text into a StringIO object if you want to be able to
    # read from it the way you would a file.
	

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
