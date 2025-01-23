
def checking(str1, str2):
    return str1 in str2  


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")


if checking(string1, string2):
    print(f'"{string1}" is found in "{string2}".')
else:
    print(f'"{string1}" is not found in "{string2}".')

