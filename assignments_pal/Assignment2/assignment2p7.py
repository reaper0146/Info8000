#Soumya Pal
#Assignment 2 part 7

import math

class Point2D:

  def __init__(self, x, y):
      self.x = float(x)
      self.y = float(y)
  
  def __str__(self):
      return "({self.x}, {self.y})".format(self=self)

class Line2D:
    
  def __init__(self, A, B):
      self.A = A
      self.B = B
      #self.dist = self.length()
  
  def __str__(self):
      return f"Points: [({self.A.x}, {self.A.y}), ({self.B.x}, {self.B.y})]\nLength {self.length()}"
  
  def length(self):
      dist = round(math.sqrt((self.B.y - self.A.y)**2 + (self.B.x - self.A.x)**2),2)
      return dist

class Triangle2D:
    
  def __init__(self, A, B, C):
      self.A = A
      self.B = B
      self.C = C
  
  def __str__(self):
      return f"Points: [({self.A.x}, {self.A.y}), ({self.B.x}, {self.B.y}), ({self.C.x}, {self.C.y})]\nPerimeter {self.perimeter()[0]}\nArea {self.area()}"
  
  def perimeter(self):
      a = Line2D(A,B).length()
      b = Line2D(B,C).length()
      c = Line2D(C,A).length()
      p = a + b + c
      return p, a, b, c

  def area(self):
      p, a, b, c = self.perimeter()
      s = p/2
      ar = round(math.sqrt(s * (s-a) * (s-b) * (s-c)),2)
      return ar


A = Point2D(-2,2)
B = Point2D(1,5)
C = Point2D(6,-1)
print(A)
print(B)
print(C)
print(Line2D(A,B))
print(Line2D(B,C))
print(Line2D(A,C))
print(Triangle2D(A,B,C))
print("\n")