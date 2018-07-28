def isValidWalk(walk):
  ne = 0
  sw = 0
  for item in walk:
    if item == 'n' or item == 'e':
      ne += 1
    else:
      sw -= 1
  print(ne, sw)
  if ne + sw == 0:
    return True
  else: 
    return False

print(isValidWalk(['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's']))
