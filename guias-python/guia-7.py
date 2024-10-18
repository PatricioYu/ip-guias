from array import *

#1.a usando listas
def pertenece (lista: list[int], e: int) -> bool:
  for i in lista:
    if (i % e) == 0:
      return True
  return False

#1.b
