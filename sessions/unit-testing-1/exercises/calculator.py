class Calculator:

  def __init__(self, x, y, operator):
    self.x = x
    self.y = y
    self.operator = operator

  def add(self):
    return self.x + self.y

  def subtract(self):
    return self.x - self.y

  def multiply(self):
    return self.x * self.y

  def divide(self):
    return self.x / self.y

  def check_valid_input_type(self):
    if not isinstance(self.x, (int, float)) or \
        not isinstance(self.y, (int, float)):
        raise TypeError('You entered an invalid type')
    else:
      return True
      
  def check_valid_input_range(self):
    if (self.x < -100000 or self.x > 100000) or \
        (self.y < -100000 or self.y > 100000):
        raise ValueError('Number out of range')
    else:
      return True

  def calculate(self):
    if self.check_valid_input_type() and \
        self.check_valid_input_range():
        if self.operator == "+":
          return self.add()
        elif self.operator == "-":
          return self.subtract()
        elif self.operator == "*":
          return self.multiply()
        elif self.operator == "/":
          return self.divide()
        else:
          if self.operator not in "+-*/":
            message = "That is an incorrect operator."
            raise ValueError(message)
          

my_calc = Calculator(5, 5, "*")
print(my_calc.calculate())
