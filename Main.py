from typing import List

def merge_sort(data) -> None:
  # Write code here
  if len(data) > 1:
    mid = len(data)//2
    left_array = data[:mid]
    right_array = data[mid:]
    
    merge_sort(left_array)
    merge_sort(right_array)
    
    i=0
    j=0
    k=0
    
    while i < len(left_array) and j < len(right_array):
      if left_array[i] <= right_array[j]:
        data[k] = left_array[i]
        i += 1
      else:
        data[k] = right_array[j]
        j += 1
      k += 1

    while i < len(left_array):
      data[k] = left_array[i]
      i += 1
      k += 1

    while j < len(right_array):
       data[k]=right_array[j]
       j += 1
       k += 1


# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data)
print(data)
