from array import *

#1.a usando listas
def pertenece (lista: list[int], e: int) -> bool:
  for i in lista:
    if i == e:
      return True
  return False

print(f'pertenece([1,2,3,4,5],4): {pertenece([1,2,3,4,5],4)}')
print(f'pertenece([1,2,3,4,5],0): {pertenece([1,2,3,4,5],0)}')

#1.b
def divide_a_todos (l: list[int], e: int) -> bool:
  for i in l:
    if (i % e) != 0:
      return False
  return True

print(f'divide_a_todos([1,2,3,4,5,6], 1): {divide_a_todos([1,2,3,4,5,6], 1)}')
print(f'divide_a_todos([1,2,3,4,5,6], 2): {divide_a_todos([1,2,3,4,5,6], 2)}')

#1.c
def suma_total (l: list[int]) -> int:
  sum: int = 0
  for i in l:
    sum += i

  return sum

print("suma_total([1,2,3,4,5]):", suma_total([1,2,3,4,5]))

#1.d
def maximo (l: list[int]) -> int:
  max: int = l[0]
  for i in l:
    if i >= max:
      max = i
  return max

print("maximo([4,2,3,1,5,1]):", maximo([4,2,3,1,5,1]))

#1.e
def minimo (l: list[int]) -> int:
  min: int = l[0]
  for i in l:
    if i <= min: min = i
  return min

print("minimo([4,2,3,1,5]):", minimo([4,2,3,1,5]))

#1.f
def ordenados (l:list[int]) -> bool:
  cont: int = 0

  while cont < len(l)-1:
    if (l[cont] > l[cont+1]): return False

    cont += 1

  return True

print("ordenados([1,2,3,4,5])", ordenados([1,2,3,4,5]))
print("ordenados([1,2,3,5,4])", ordenados([1,2,3,5,4]))

#1.g
def pos_max (l: list[int]) -> int:
  pos_max: int = -1
  max: int = l[0]

  for i in range(1,len(l)):
    if l[i] >= max:
      pos_max = i
      max = l[i]

  return pos_max

print("pos_max([1,2,3,4,5])", pos_max([1,2,3,4,5]))
print("pos_max([1,2,3,4,5])", pos_max([5,2,3,4,1]))
print("pos_max([1,2,5,3,4])", pos_max([1,2,5,3,4]))
print("pos_max([5,2,5,3,4])", pos_max([5,2,5,3,4]))

#2.a
def cerosEnPosPares (l: list[int]) -> list[int]:
  for i in range(len(l)):
    if i % 2 == 0:
      l[i] = 0

  return l

a: list[int] = [1,2,3,4,5]

print("cerosEnPosPares(a)", cerosEnPosPares(a), "original list", a)

#2.b
def cerosEnPosPares2 (l:list[int]) -> list[int]:
  newList: list[int] = list(l)

  for i in range(len(newList)):
    if i % 2 == 0:
      newList[i] = 0

  return newList

b: list[int] = [1,2,3,4,5]

print("cerosEnPosPares2(b)", cerosEnPosPares2(b), "lista original", b)

#2.c
def borrarVocales (palabra: str) -> str:
  vocales: list[str] = "aeiouAEIOU"

  letras: list[str] = list(palabra)

  palabraSinVocales: list[str] = ""

  for l in letras:
    if l not in vocales:
      palabraSinVocales = palabraSinVocales + l

  return palabraSinVocales

print("borrarVocales('caracoles')", borrarVocales("caracoles"))

#2.d
def reemplazaVocales (p: list[str]) -> list[str]:
  pass

#2.e
def daVueltaStr (p: list[str]) -> list[str]:
  palabraInvertida: str = ""

  for i in range(len(p)):
    palabraInvertida += p[len(p)-i-1]

  return palabraInvertida

print("daVueltaStr('hola')", daVueltaStr("hola"))

#2.f
def eliminarRepetidos (p:list[str]) -> list[str]:
  pass

#3.a
def pertenece_a_cada_uno_version_1 (l:list[list[int]], e: int) -> bool:
  for i in l:
    if e in i:
      return True

  return False

print(pertenece_a_cada_uno_version_1([[1,2,3,4],[2,3],[5]], 5))