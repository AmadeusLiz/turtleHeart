from turtle import *

def curva():
  for i in range(200):
    right(1)
    forward(1)

color('red') # Personalizable!
begin_fill()
left(140)
forward(111.65)
curva()
left(120)
curva()
forward(111.65)
end_fill()

print('Mensaje')
