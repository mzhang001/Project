import sys

filePath = sys.argv[1]
delimiter = sys.argv[2]

print filePath
print delimiter

names = filePath.split(delimiter)

return names[len(names) - 1]
