import random
# ------------
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# -----------------------------------------------------------------------------------------------------------------------------------------------
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# ------------------------------------------------------------------
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']
# ------------------------------------------------------------------
print("Generátor hesel!")
# ------------------------
my_password = []

# počet písmen
choice_letter = int(input("Kolik písmen chcete mít ve svém heslu?\n"))
for one_letter in range(0,choice_letter):
    one_letter = random.choice(letters)
    my_password.append(one_letter)
    
# počet čísel
choice_number = int(input("Kolik čísel chcete mít ve svém heslu?\n"))
for one_number in range(0,choice_number):
    one_number = random.choice(numbers)
    my_password.append(one_number)

# počet symbolů
choice_mark = int(input("Kolik speciálních znaků chcete mít ve svém heslu?\n"))
for one_mark in range(0,choice_mark):
    one_mark = random.choice(special_char)
    my_password.append(one_mark)

print(my_password)

new_password = ""

for one_password in my_password:
    new_password += one_password
    
    
print(new_password)    
    