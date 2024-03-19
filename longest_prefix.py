
def Longest_prefix(strings):
    i = 0
    minstrings=min(strings,key=len)
    minsize = len(minstrings)
    while (i < minsize and strings[0][i] == strings[1][i] == strings[2][i]):
        i +=1
    result = strings[0][0:i]
    return result
      

strings=list()
while len(strings) !=3:
    strings.append(input("please write a list of words :"))
    print(strings)    
print(Longest_prefix(strings))   