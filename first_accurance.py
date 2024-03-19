

haystack = "sadbutsad"
needle = "sad"

def first_accurance(needle,haystack):
    if len(needle) > len(haystack):
            return -1
    for i in range(len(haystack) -1):
           if haystack[i:len(needle)+1] == needle :
            return i
           
    # return -1


print(first_accurance(needle,haystack))


    

