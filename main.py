#class Human:
    #def __init__(self):
      #self.name = 'none'
      #self.age = 0
      #self.gender = 'None'
    #def introduce(self):
      #print('Hello, my name is', self.name)
    #def add_info(self):
      #self.name = input('Name: ')
      #self.age = int(input('Age: '))
      #self.gender = input('gender:')

#obj = Human()
#obj.add_info()
#obj.intoduce()

from random import *


class Student:
  def __init(self, name):
    self.name = name
    self.glandness = 50
    self.progress = 0
    self.alive = True

  def study(self):
    print('Study time')
    self.progress += 0.12
    self.glandess -= 5

  def sleep(self):
    print('Sleep time')
    self.glandess += 3

  def chill(self):
    print('chill time')
    self.glandess += 5
    self.progress -= 0.1

  def is__alive(self):
    if self.progress < -0.5:
      print('Soooo bad')
      self.alive = false
    elif self.gladness <= 0:
      print('Depression...')
      self.alive = false
    elif self.progress > 5:
      print('Passed the exam!')
      self.alive = false
    def end(self):
      print('glandess:', self.gladness)
      print('Progress:', self.progress)
    def live(self):
      print('Day:', day)
      live_cube = randit(1,3)
      if live-cube == 1:
        self.study()
      elif live_cube == 2:
        self.sleep()
      elif live_cube == 3:
        self.shill()
      self.end()
      self.is_alive()

obj = Student('Bob')
for day in range(365):
  if obj.alive == false:
    break
  obj.live(day)