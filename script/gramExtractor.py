import sys
import re
path = "/home/mz342/Project/"
#print(sys.argv)

fileName = sys.argv[1]
targetWord = sys.argv[2]
outputDir = sys.argv[3]
#print fileName
#print targetWord



#fileName = path + fileName

f = open(fileName,"r")
out_f = open(outputDir + targetWord + ".txt", "a")
targetWord = targetWord
line = f.readline()

#i = 0
flag = False
while line != "":
	line = line.lower()
	
	tokens = re.split(r'[ \t]', line)
	#print tokens[0]
	for i in range(len(tokens) - 1):
		if tokens[i] == targetWord:
			out_f.writelines(line)
			break
		#i += 1
		#flag = True
		
		#out_f.writelines("\n")
	#elif flag:
	#	break
	#if i == 1000:
	#	break	
	line = f.readline()
f.close()
out_f.close()
