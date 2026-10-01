#TASK1-TEMPERATURE CONVERTER
while True:

    try:
        celsius=float(input("Enter the celsius temperature you want to convert: "))
        fahrenheit=float(input("Enter the fahrenheit temperature you want to convert: "))
        break
    except ValueError:
            print("Invalid number. Enter a number")
def celsius_to_fahrenheit(celsius):
    fahrenheit=celsius*9/5 +32
    print(f"The temperature in fahrenheit is {fahrenheit}")

def fahrenheit_to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    print(f"The temperature in celsius is {celsius}")

celsius_to_fahrenheit(celsius)
fahrenheit_to_celsius(fahrenheit)

#TASK2-AGE CALCULATOR
while True:
     try:
          birth_year=int(input("Enter the year of birth: "))
          current_year=int(input("Enter the current year:"))

          if birth_year>current_year:
               print("This information are not valid")

               continue
          break
     except ValueError:
          print("Make sure but year of birth and current year are numbers")


def calculate_age(birth_year, current_year):
     age=current_year-birth_year
     
     print(f"The age is {age}")
     return age

age=calculate_age(birth_year, current_year)

def can_vote(age):
     if age >= 18:
          print("The user can vote")
     else:
          print("The user cannot vote")


can_vote(age)

#TASK3-PASSWORD STRENGTH CHECKER
def check_password(password):


    if len(password) < 8:
        print("Password must be at least 8 characters")
        return


    has_digit = False
    has_lower = False
    has_upper = False


    for character in password:

        if character.isdigit():
            has_digit = True

        if character.islower():
            has_lower = True

        if character.isupper():
            has_upper = True


    missing = []

    if not has_digit:
        missing.append("a number")

    if not has_lower:
        missing.append("a lowercase letter")

    if not has_upper:
        missing.append("an uppercase letter")


    requirement_met = has_digit + has_lower + has_upper


    if requirement_met <= 1:
        strength = "Weak"

    elif requirement_met == 2:
        strength = "Medium"

    else:
        strength = "Strong"

    print(f"Password is {strength}")


    if missing:
        print(f"Missing: {', '.join(missing)}")
    else:
        print("All requirements met")



password = input("Enter your password: ")


check_password(password)

#TASK4-SHOPPING CART TOTAL 
product1=15000
product2=25000
product3=10000
def calculate_subtotal(product1, product2, product3):

    subtotal= product1+product2+product3
    print(f"The subtotal of the products is {subtotal}")
    return subtotal

subtotal=calculate_subtotal(product1, product2, product3)

def calculate_discount(subtotal):
    if 0<=subtotal<=20000:
        discount=0

    elif 20001<=subtotal<=50000:
        discount= 0.05*subtotal
        print(f"You have a discount of 5%, and you will be charged {discount} less")

    else:
        discount=0.1*subtotal
        print(f"You have a discount of 10%, and you will be charged {discount} less")
    return discount

discount=calculate_discount(subtotal)

def calculate_Finaltotal(subtotal, discount):
    finaltotal=subtotal-discount
    print(f"the finaltotal you are to pay is {finaltotal}")

calculate_Finaltotal(subtotal,discount)

#TASK5-NUMBER ANALYZER

def number_analyzer(number):
    if number>0:
        print(f"{number} is positive")
    elif number <0:
        print(f"{number} is negative")
    else:
        print("The number is zero")



    if number%1==0:
        print("integer")
        if number %2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")

    else:
        print("decimal")

number=float(input("Enter the number:"))
number_analyzer(number)