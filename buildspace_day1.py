#TASK1-PERSONAL PROFILE
name="Newton"
age=24
country="Nigeria"
is_student=True
favorite_language="C"
years_of_coding=1
print(f"My name is {name}, I am {age} years old chad from {country}, am I a student? {is_student}, the programming language I love the most is {favorite_language} though I love python but I still prefer {favorite_language} over it, it has been {years_of_coding} year(s) have been coding")
age_in_5_years=age+5
age_in_10_years=age+10
age_in_20_years=age+20
print(f"I will be {age_in_5_years} in 5 years")
print(f"I will be {age_in_10_years} in 10 years")
print(f"I will be {age_in_20_years} in 20 years")

#TASK2-SIMPLE CALCULATOR

first_number=20
second_number=3
addition=first_number+second_number
subtraction=first_number-second_number
multiplication=first_number*second_number
division=first_number/second_number
remainder=first_number%second_number
print(f"The addition function of {first_number} and {second_number} is {addition} ")
print(f"The subtraction function of {first_number} and {second_number} is {subtraction} ")
print(f"The multiplication function of {first_number} and {second_number} is {multiplication} ")
print(f"The division function of {first_number} and {second_number} is {division} ")
print(f"The remainder function of {first_number} and {second_number} is {remainder} ")

#TASK3-STUDENT GRADE CALCULATOR

English=78
Mathematics=85
Python=92
Design=70
total=English+Mathematics+Python+Design
average=total/4
if 90<=average<=100:
    print("The grade is A")
elif 80<=average<=89:
    print("The grade is B")
elif 70<=average<=79:
    print("The grade is C")
elif 60<=average<=69:
    print("The grade is D")
elif 50<=average<=59:
    print("The grade is E")
elif 0<=average<=49:
    print("The grade is F")
else:
    print("Invalid grade")

#REUSEABLE FUNCTION

def calculate_grade(average):
    if 90<=average<=100:
     print("The grade is A")
    elif 80<=average<=89:
     print("The grade is B")
    elif 70<=average<=79:
      print("The grade is C")
    elif 60<=average<=69:
     print("The grade is D")
    elif 50<=average<=59:
     print("The grade is E")
    elif 0<=average<=49:
      print("The grade is F")
    else:
     print("Invalid grade")

calculate_grade(average)

#TASK4-LOGIN VALIDATOR

username="admin"
password="12345"
input1=input("Enter the username: ")
if input1=="":
   print("Username can not be empty")
else:
    input2=input("Enter your password: ")
    if input2=="":
      print("password can not be empty")
    else:
        if len(input2)<5:
            print("Password must contain at least 5 character")

        else:
           if username==input1 and password==input2:
              print("Login successful")
           else:
              print("Invalid username or password") 


#TASK5_MINI EXPENSE CALCULATOR
food=5000
transport=3000
internet=7000
entertainment=4000
income=100000
total_expenses=food+transport+internet+entertainment
print(f"the total expenses is {total_expenses}")
average_expense=total_expenses/4
print(f"The average expense is {average_expense}")
highest=0
if food > transport and food>internet and food>entertainment:
   highest=food
   
elif transport > internet and transport>entertainment and transport>food:
   highest=transport
   
elif internet > entertainment and internet>food and internet>transport:
   highest=internet
   
else:
   highest=entertainment

print(f"The highest expense is {highest}")

remaining_money=income-total_expenses
print(f"The money left is {remaining_money}")

def calculate_expenses(food, transport, internet,entertainment,income):
   
   total_expenses=food+transport+internet+entertainment
   average_expense=total_expenses/4
   
   if food > transport and food>internet and food>entertainment:
        highest=food
   
   elif transport > internet and transport>entertainment and transport>food:
        highest=transport
   
   elif internet > entertainment and internet>food and internet>transport:
        highest=internet
   
   else:
        highest=entertainment

   remaining_money=income-total_expenses


   print(f"the total expenses is {total_expenses}")
   print(f"The average expense is {average_expense}")
   print(f"The highest expense is {highest}")
   print(f"The money left is {remaining_money}")

calculate_expenses(food, transport, internet,entertainment,income)
