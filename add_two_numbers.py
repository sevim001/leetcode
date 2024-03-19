# Definition for singly-linked list.

  
list1 = [1, 5, 6, 9, 11]
list2 = [3, 4, 7, 8, 10]
def Add_two_numbers( list1:list , list2:list) ->list:
 OurFinalList=[]
 i =0
 j=0
 while i<len(list1) and j<len(list2):
        if list1[i] < list2[j]:
            OurFinalList.append(list1[i])
            i+=1
        else:
            OurFinalList.append(list2[j])  
            j+=1

 OurFinalList = OurFinalList + list1[i:] + list1[j:] 

 return  OurFinalList 

print(Add_two_numbers(list1,list2))

                