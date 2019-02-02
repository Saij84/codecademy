class Circle:
  pi = 3.14

  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2

  def circumference(self):
    circumference = 2.0 * self.pi * self.radius
    return circumference


medium_pizza = Circle(12)
medium_pizza.circumference()
teaching_table = Circle(36)
teaching_table.circumference()
round_room = Circle(11460)
teaching_table.circumference()
