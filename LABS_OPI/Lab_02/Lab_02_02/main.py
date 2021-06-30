from iarray import *

def test_1():
  arr = list()
  
  arr.append(0)
  arr.append(5)
  arr.append(3)
  arr.append(8)
  
  return arr, 4


def main():
  arr, n = test_1()

  print_array(arr, n)
  
  print("Max pos = " + str(get_max_pos(arr, n)))


if __name__ == '__main__':
  main()