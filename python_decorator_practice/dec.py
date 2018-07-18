def heading (message_function):
  def final_function():
    return '<h1>{0}</h1>'.format(message_function())
  return final_function

@heading
def message():
  return "Nashville Software School"

print(message())