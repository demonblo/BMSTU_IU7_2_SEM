from iarray import *

#Программа возвращает пару значений массива и количества элементов этого массива 
def test_1():
  arr = list()
  
  arr.append(0)
  arr.append(-1)
  arr.append(3)
  arr.append(-2)
  arr.append(5)
  
  return arr, 5

def test_2():
  arr = list()
  
  arr.append(0)
  arr.append(-1)
  arr.append(-3)
  arr.append(-2)
  arr.append(2)
  arre.appen(-10)

  return arr, 6

# Программа выводит с помощью функции print_array массив и количество его элементов
# и с помощью функции form_array удаляет из массива все отрицательные элементы и выводит исправленный массив
def main():
  arr, n = test_1()

  print("Source")
  print_array(arr, n)
  
  new_arr, new_n = form_array(arr, n)

  print("Result")
  print_array(new_arr, new_n)


if __name__ == '__main__':
  main()
