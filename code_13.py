def get_merge_sorted_list(unsorted_list):
    
    #pass #Remove this line of code and implement your merge sort algorithm
    if len(unsorted_list) == 1:
        return unsorted_list
    
    mid_point = int((len(unsorted_list))//2)

    right_side = unsorted_list[:mid_point]
    left_side = unsorted_list[mid_point:]

    half_right = get_merge_sorted_list(right_side)
    half_left = get_merge_sorted_list(left_side)

    merge=  half_right + half_left 
    return merge
#secondfunction 
    
def sorted_list(first, second):
  final_list= []
  a=0
  b=0

  while a < len(first) and b< len(second): 
    final_list = []
    
    if first[0] < second[0]:
        final_list.append(first[0])
    
    else:
        final_list.append(first[b])
      

  if len(first):
       final_list.append += first
  if len(second):
       final_list.append += second

  return (final_list)


if __name__ == "__main__":

    unsorted_list = [2, 4, 3, 8, 5, 10, 1,6]
    sorted= get_merge_sorted_list(unsorted_list)
    print(sorted)
