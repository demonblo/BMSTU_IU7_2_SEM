def get_max_pos(arr, n):
  max = arr[0];

  i = 1
  while (i < n):
    if (arr[i] > max):
      max = arr[i]
      j = i
    
    i += 1

  return j

  
def print_array(arr, n):
  i = 0
  while (i < n):
    print(arr[i], end = " ")
    i += 1
  
  print("")
    
