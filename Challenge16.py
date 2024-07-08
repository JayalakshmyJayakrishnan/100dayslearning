def print_full_name(first, last):
    a = f"{first} {last}"                                         #Combine the first and last names with a space in between
    print(f"Hello {a}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()                                          #Prompt the user to enter their first name and last name
    last_name = input()
    print_full_name(first_name, last_name)
