name_list = [
  {'name':'Katie'},
  # {'name':'Paul'}
  # {'name':'James'},
  # {'name':'Pen Pen'}
  ]

# Get list of names like this: ['Katie', 'Paul', 'James', 'Pen Pen']
def namelist(name_list):
  just_names = []
  for name_dict in name_list:
    just_names.append(name_dict['name'])

  if len(just_names) == 1:
    # return f'{just_names[0]}'
    return ('%s' %just_names[0])
  elif len(just_names) == 2:
    return ("" " & ".join(just_names))
  elif len(just_names) >= 2:
    return f'{", ".join(just_names[0:-1])} & {just_names[-1]}'
  # else len(just_names) < 1:
  #   return ''

print(namelist(name_list))