class Test:
  def __init__(self):
    self.a = 1

  def __setitem__(self, a, b):
    self.a = b

  def __getitem__(self, b):
    return self.a