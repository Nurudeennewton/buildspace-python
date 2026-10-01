'''#TASK!-ARRAY BASICS
languages=["Javascript", "Python", "Java", "C#", "Go", "PHP", "Ruby", "Typescript"]
print(languages[0])
print(languages[-1])
print(languages[3])
print(len(languages))
languages[0]="C++"
print(languages)
languages.append("Javascript")
languages.pop(4)
print(languages)
print(languages[12]) #list index of range

#TASK2-STUDENT SCORE ANALYZER
def analyze_scores(scores):
    total = analyze_total(scores)
    average = average_score(total, scores)
    highest = highest_score(scores)
    lowest = lowest_score(scores)
    passed = count_passed(scores)
    failed = count_failed(scores, passed)

    return total, average, highest, lowest, passed, failed

def analyze_total(scores):
    total=0
    for score in scores:
        total=total+score
        
    return total

def average_score(total, scores):
    average_score=total/len(scores)
    return average_score

def highest_score(scores):
    highest_score=max(scores)
    return highest_score


def lowest_score(scores):
    lowest_score=min(scores)
    return lowest_score

def count_passed(scores):
    passed=0
    
    for score in scores:
        if score >=50:
            passed=passed+1

    return passed

def count_failed(scores, passed):
    failed=len(scores)-passed
    return failed
    



scores=[78, 92, 25, 88, 54, 34, 96, 83]

total, average_score, highest, lowest, passed, failed=analyze_scores(scores)

print(f"The total score is {total}")

print(f"The average score is {average_score}")

print(f"The highest score is {highest}")

print(f"The lowest score is {lowest}")

print(f"{passed} score passed")

print(f"{failed} score failed")


#TASK3-SHOPPING CART
products = [
    {"name": "Keyboard", "price": 15000},
    {"name": "Mouse", "price": 8000},
    {"name": "Monitor", "price": 75000},
    {"name": "Headphones", "price": 20000},
    {"name": "USB Cable", "price": 3000}
]
print(len(products))
total=0
most_expensive=products[0]
least_expensive=products[0]
for product in products:
    total=total+product["price"]
print(f"The total of product is {total}")
for product in products:
    if product["price"]>most_expensive["price"]:
        most_expensive=product
print(most_expensive)
for product in products:
    if product["price"]<least_expensive["price"]:
        least_expensive=product
print(least_expensive)
#adding quantity to product
for product in products:
    quantity=int(input(f"Enter the quantity of {product['name']}: "))
    product["quantity"]=quantity
print(products)

actual_cart_total=0
for product in products:
    product_total=product["price"]*product["quantity"]
    actual_cart_total=actual_cart_total+product_total
print(f"The actual cart total is {actual_cart_total}")

#TASK4-ARRAY SEARCH

users=[
    {"name":"Newton", "email":"newton@gmail.com","role":"admin"},
    {"name":"Hackim", "email":"engineer@gmail.com","role":"admin"},
    {"name":"Gaius", "email":"nerd@gmail.com","role":"user"},
    {"name":"mathesis", "email":"summayh@gmail.com","role":"user"}

]

def find_user_by_email(users, email):
    for user in users:
        if user["email"] == email:
            return user
        else:
            return None

email = input("Enter the user's email: ")

user = find_user_by_email(users, email)

if user != None:
    print(f"User found {user}")
else:
    print("User not found")

def find_admins(users):
    admins=[]

    for user in users:
        
        if user["role"]=="admin":
            admins.append(user)

    return admins

admins=find_admins(users)
for admin in admins:
    print(admin)

def user_exists(users, email):
    for user in users:
        if user["email"] == email:
            return True

        else:
            return False


email = input("\nEnter an email to check: ")

if user_exists(users, email):
    print("User exists")
else:
    print("User does not exist")

def find_users_by_role(users, role):
    matching_users = []

    for user in users:
        if user["role"] == role:
            matching_users.append(user)

    return matching_users


role = input("Enter a role to search for: ")

matching_users = find_users_by_role(users, role)

if len(matching_users) > 0:
    print(f"Users with role '{role}':")
    for user in matching_users:
        print(user)
else:
    print(f"No users found with the role '{role}'")'''

# TASK 5 - ARRAY TRANSFORMATION

def apply_discount(prices):
    discounted_prices = []
    for price in prices:
        discounted_price = price * 0.9
        discounted_prices.append(discounted_price)
    return discounted_prices


def prices_above(prices):
    result = []
    for price in prices:
        if price > 5000:
            result.append(price)
    return result


def prices_below(prices):
    result = []
    for price in prices:
        if price < 5000:
            result.append(price)
    return result


def sort_prices(prices):
    sorted_prices = prices.copy()  # keeps the original list unchanged

    for i in range(len(sorted_prices)):
        for j in range(0, len(sorted_prices) - i - 1):
            if sorted_prices[j] > sorted_prices[j + 1]:
                temporary = sorted_prices[j]
                sorted_prices[j] = sorted_prices[j + 1]
                sorted_prices[j + 1] = temporary

    return sorted_prices


def array_transformation():
    prices = [1000, 2500, 5000, 7500, 10000]

    print("Discounted prices:", apply_discount(prices))
    print("Prices above 5000:", prices_above(prices))
    print("Prices below 5000:", prices_below(prices))
    print("Sorted prices:", sort_prices(prices))


array_transformation()