import datetime

user_name = input('What\'s your name? ')
user_age = input('What\'s your age? ')
message_print_number = input('How many times do you want to know it? ')

current_time = datetime.datetime.now()

year_to_turn_100 = int(current_time.year) - int(user_age) + 100

# Need user name and years until user turns 100.
for i in range(0, int(message_print_number)):
  print(f'{user_name} will turn 100 in the year {year_to_turn_100}')