#my predictions before running
# 17 / 5        = 3.4
# 17 // 5       = 3
# 2 ** 5        = 32
# 7 + 3 * 2     = 13
# (7 + 3) * 2   = 20

print(17 / 5)
print(17 // 5)
print(2 ** 5 )
print(7 + 3 * 2)
print((7 + 3) * 2)

# In my own words, / gives..., // gives..., % gives:
# / gives normal division and can give a decimal.
# // gives whole-number division by removing the decimal part.
# % gives the remainder after division.

print(type(10 / 2))

#TASK 2
movie_minutes = 135
hours = movie_minutes // 60
minutes_left = movie_minutes % 60
print(f"{movie_minutes} minutes is {hours} hours and {minutes_left}minutes")

#TASK 3
print(48 % 2 == 0)
print(37 % 3 == 0)

#TASK 4
x = 15
y = 20

print(x > y)
print(x < y)
print(x == y)
print(x != y)
print(x >= 15)
print(y <= 19)

#TASK 5
age = 16
has_ticket = True
is_vip = False

#my prediction for can_enter: False

can_enter = has_ticket and (age >= 18 or is_vip)
print(can_enter)

age = 20
can_enter = has_ticket and (age >= 18 or is_vip)
print(can_enter)

#TASK 6
balance = 100

#my prediction for the final balance is 240

balance += 50
balance -= 30
balance *= 2

print(balance)

#TASK 7
quote = "He said, 'Python is amazing!'"
print(quote)

contraction = "It's not a problem"
print(contraction)

#I used double quotes for contraction so that the apostrophe can be 
# included inside the string without ending the string.

greeting = "Good" + " " + "day ladies and gentle" + "!"
print(greeting)

print("-" * 20)

#TASK 8
messy_name = "  grace HOPPER    "

print(f"[{messy_name}]")
print(f"[{messy_name.lstrip()}]")
print(f"[{messy_name.rstrip()}]")
print(f"[{messy_name.strip()}]")

clean_name = messy_name.strip()

print(clean_name.title())
print(clean_name.upper())
print(clean_name.lower())

print(messy_name)

#TASK 9 
item = "pencil"
price = 1.5
quantity = 12

print(f"{quantity} {item}(s) cost {price * quantity} in total")

#TASK 10 
word = "programming"

# Predictions:
# First character = p
# Last character = g
# First three characters = pro
# From index 3 = gramming
# Reversed = gnimmargorp
# Every second character = pormig

print(word[0])
print(word[-1])
print(word[:3])
print(word[3:])
print(word[::-1])
print(word[::2])

#TASK 11

raw_first = "  ada "
raw_last = " LOVELACE  "
score_1 = 78
score_2 = 92
score_3 = 85
attendance_percent = 80

first_name = raw_first.strip().title()
last_name = raw_last.strip().title()

full_name = f"{first_name} {last_name}"

average_score = (score_1 + score_2 + score_3) / 3

passed = average_score >= 60 and attendance_percent >= 75

initials = (first_name[0] + last_name[0]).upper()

username = first_name.lower() + last_name[:3].lower()

print("=" * 30)
print(f"Name: {full_name}")
print(f"Initials: {initials}")
print(f"Username: {username}")
print(f"Average: {average_score}")
print(f"Passed: {passed}")
print("=" * 30)


#This follows the assignments restrictions: **no input(), no if statements, and no loops**.

#The expected final ID card will show **Ada Lovelace, AL, adalov, 85.0, and True**, matching the required format.
