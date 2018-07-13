num = int(input('Type a number: '))

if num == 0:
  print('Neither odd nor even.')
elif num % 2 == 0:
  print('That number is even!')
elif num % 2 == 1:
  print('That number is odd!')