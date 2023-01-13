# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
  x,y,z = sorted([a,b,c])
  print(x,y,z)
  if z >= x + y: return 0
  if z*z == x*x + y*y: return 2
  return 1 if z*z < x*x + y*y else 3
