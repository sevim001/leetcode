def last_word(string):
    string = string.strip()
    reversed_string= reversed(string)    
    word=""
    for i in reversed_string: 
        if i == " ":
            break
        else:
            word= word+i
    return len(word)        

string = "   fly me   to   the moon  "
print(last_word(string))