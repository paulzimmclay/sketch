def interior_decorator(func):
  def add_curtains():
    func()
    print('now my house has purple cutains')

  return add_curtains

def move_in():
  print('My house was empty but...')

new_house = interior_decorator(move_in)
new_house()