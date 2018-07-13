doop = open('./bottle.txt', 'a')
doop.write('doopity \r')
# file.close()

with open('./bottle.txt', 'r') as afile:
  data = afile.read()

print(data)