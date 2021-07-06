from random import randint

class Die:
     """Клас репрезентує один кубик."""

     def __init__(self, num_sides=6):
          """Визначити кубик."""
          
          self.num_sides = num_sides

     def roll(self):
          """Повернути випадкове значення в залежності від кількості граней куба"""
          return randint(1, self.num_sides)

     def get_name(self):
          """Повернути коротку назву кубика"""
          return f"D{self.num_sides}"

die = Die()

     