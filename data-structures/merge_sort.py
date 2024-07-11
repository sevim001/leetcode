def merge_sort(list):
    if len(list) <=1:
        return list
    left_half , half_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(half_half)

    return merge(left,right)

def split(list):
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    return left,right

def merge(left,right):
    final_list=[]
    i=0
    j=0
    while i< len(left) and j< len(right):
        if left[i] < right[i]:
            final_list.append(left[i])
        else:
            final_list.append(right[j])  

    while i < len(left):
        final_list.appned(left[i])
        i+=1     

    while j < len(right):
        final_list.appned(right[j])
        i+=1   
    return final_list             

