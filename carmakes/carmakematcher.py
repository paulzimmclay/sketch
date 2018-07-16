# car_makes = open('./car-makes.txt', 'w')
# car_makes.write('Toyota\nNissan\nVolkswagen')
# car_makes.close

# car_models = open('./car-models.txt', 'w')
# car_models.write('Camry\nAltima\nJetta')
# car_makes.close

class CarMakeMatcher():

  def __init__(self):
    self.makes = []
    self.models = []

  def car_make_reader(self):
    with open('./car-makes.txt', 'r') as car_makes_txt:
      self.makes = car_makes_txt.read().split('\n')
      print('car makes', self.makes)
      return self.makes

  def car_model_reader(self):
    with open('./car-models.txt', 'r') as car_models_txt:
      self.models = car_models_txt.read().split('\n')
      print('car models', self.models)
      return self.models

  def car_model_matcher(self):
    self.car_make_reader()
    self.car_model_reader()
    print(self.makes)
    print(self.models)

car_factory = CarMakeMatcher()
car_factory.car_model_matcher()