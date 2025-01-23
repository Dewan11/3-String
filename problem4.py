def remove(main, substring):
   
    return main.replace(substring, "")


main = input("Enter the main string: ")
substring = input("Enter the substring to remove: ")


result_string = remove(main, substring)


print(f'Resulting string after removing "{substring}": "{result_string}"')
