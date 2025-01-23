def lower():
    str = input("enter the string")
    str1 = ""
    for ch in str:
        if ch>= 'A' and ch<='Z':
            str1 = str1 + che(ord(ch)+32)
            else:
                str1 = str1 +ch
                return str1
print(lower())

def upper():
    str = input("enter the string")
    str1 = ""
    for ch in str:
        if ch>= 'a' and ch<='z':
            str1 = str1 + che(ord(ch)-32)
            else:
                str1 = str1 +ch
                return str1
print(upper())







            
    
