
def convert(list):
    #turn the list and make it into integers
	s = [str(i) for i in list]
	#join the integers together and add one to it
	res = int("".join(s)) +1
	#turn the integers into list
	new_list = [int(x) for x in str(res)]
	return new_list  

list = [9]
print(convert(list))

  