from iarray import *

#Данная функция создает тестовый массив и возвращает пару:Массив и его размерность.
def Test1():
  Arr = list()
  
  Arr.append(5)
  Arr.append(3)
  Arr.append(2)
  Arr.append(5)
  Arr.append(1)
  
  return Arr, 5

#Данная функция создает тестовый массив и возвращает пару значений:Массив и его размерность.
def Test2():
  Arr = list()
  
  Arr.append(5)
  Arr.append(5)
  Arr.append(2)
  Arr.append(5)
  Arr.append(1)
  Arr.append(6)
  
  return Arr, 6

#Данная функция принимает пару значений:Массив и его размерность и далее выводит ответ(Кодичество максимальных членов массива).
def main():
  Arr, N = Test1()
  Arr, N = Test2()
  
  print("Maximal value is found " + str(GetMaxCount(Arr, N)) + " times.")


if __name__ == '__main__':
  main()
