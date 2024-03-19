def RomanTranslator(Roman_word):
    dict={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
        "IV":4,
        "IX":9,
        "XL":40,
        "XC":90,
        "CD":400,
        "CM":900
    }
    
    translation=0
    for char in Roman_word:
        translation +=dict[char]   
    return translation    
        
print(RomanTranslator(input("enter the roman charecter :")))