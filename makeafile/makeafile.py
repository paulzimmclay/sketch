doop = open('./bottle.txt', 'a')
doop.write('doopity')
# file.close()

with open('./bottle.txt', 'r') as afile:
  data = afile.read()

print(data)