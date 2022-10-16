class Human:
  def __init__(self):
    self.name = 'none'
    self.age = 0
    self.gender = 'None'
  def introduce(self):
    print('Hello, my name is', self.name)
  def add_info(self):
    self.name = input('Name: ')
    self.age = int(input('Age: '))
    self.gender = input('gender:')

obj = Human()
obj.introduce()
obj.add_info()
obj.intoduce()