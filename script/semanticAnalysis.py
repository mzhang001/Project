import math

startYear = 1800
endYear = 2009
space = 5
targetWord = "dear"

intervals = (endYear - startYear) / space + 1

def yearToIndex(year):
	return (year - startYear) / space

def indexToYear(index):
	return index * space + startYear

inputFile = "/home/mz342/Project/output/5gram/" + targetWord + ".txt"
f = open(inputFile,'r')
dictmap = []

for i in range(intervals):
	dictmap.append({})

#print len(dictmap)

for line in f:
	data,year,count_single,count_book = line.split("\t")
	year = int(year)
	count_single = int(count_single)
	if (year < startYear) or (year > endYear):
		continue
	index = yearToIndex(year)
	#print index
	
	mapAtIndex = dictmap[index]
	words = data.split(" ")
	for word in words:
		if word == targetWord:
			continue
		#print word
		if(word not in mapAtIndex):
			(dictmap[index])[word] = count_single
		else:
			(dictmap[index])[word] += count_single
	#break
f.close()

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

for i in range(intervals - 1):
	year = indexToYear(i)
	print year," ",indexToYear(i+1)," ",get_cosine(dictmap[i],dictmap[i+1])
	#for j in range(i + 1,intervals):
	#	print str(year), " ", str(indexToYear(j)), " ", get_cosine(dictmap[i],dictmap[j])	
	#for key in dictmap[i]:
	#	print year," ",key," ",dictmap[i][key]






