import math

startYear = 1950
endYear = 2009
space = 10
targetWord = "mouse"

intervals = (endYear - startYear) / space + 1

def yearToIndex(year):
	return (year - startYear) / space

def indexToYear(index):
	return index * space + startYear

inputFile = "/home/mz342/Project/output/5gram/mouse.txt"
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
	#for j in range(i + 1,intervals):
	#	print year," ",indexToYear(j)," ",get_cosine(dictmap[i],dictmap[j])
	for key in dictmap[i]:
		print year," ",key," ",dictmap[i][key]






