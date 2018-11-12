from enum import Enum

class Test(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    def __init__(self, _constructed_piece):
        self.prev = None


class Test2:
    def __init__(self, x):
      self.name = x
      print(func1(self))
      return

def func1(object_test2):
  return object_test2.name
