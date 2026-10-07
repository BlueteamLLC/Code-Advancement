# Assignment 02c + 03: Operators & Strings
# Name: JIDEOFOR CHINEDU
# Group: BLUE
# Run with: python assignment.py
# Read assignment.md for the full instructions.


# ===============================================================
# PART 1: OPERATORS
# ===============================================================

# ---------------- PART A: ARITHMETIC ----------------

# TASK 1
# My predictions (BEFORE running):
#   17 / 5       -> 3.4
#   17 // 5      -> 3
#   17 % 5       -> 2
#   2 ** 5       -> 32
#   7 + 3 * 2    -> 13
#   (7 + 3) * 2  -> 20
# TODO: print each of the six expressions
print(17 / 5)
print(17 // 5)
print(17 % 5)
print(2 ** 5)
print(7 + 3 * 2)
print((7 + 3) * 2)

# In my own words, / gives..., // gives..., % gives...:
# TODO:
/ gives the quotient of a division as a float
// gives the quotient as an integer (floor division)
% gives the remainder of a division.

# TODO: print(type(10 / 2)) and say if it surprised you
<class 'float'>. It did not surprise me because division in Python always results in a float, even if the result is a whole number.

# TASK 2
movie_minutes = 135
# TODO: hours = 
hours = movie_minutes // 60
# TODO: minutes_left = movie_minutes % 60
minutes_left = movie_minutes % 60
# TODO: print the sentence with an f-string
print(f"The movie is {hours} hours and {minutes_left} minutes long.")


# TASK 3
# TODO: print whether 48 is even (use % and ==)
print(48 % 2 == 0)
# TODO: print whether 37 is even
print(37 % 2 == 0)
# Why does the remainder after dividing by 2 tell us this?
# TODO:
because if a number is even, it will have no remainder when divided by 2, while an odd number will have a remainder of 1.


# ---------------- PART B: COMPARISON & LOGIC ----------------

# TASK 4
x = 15
y = 20
# TODO: print x > y, x < y, x == y, x != y, x >= 15, y <= 19
print(x > y)
print(x < y)
print(x == y)
print(x != y)
print(x >= 15)
print(y <= 19)
# Difference between = and == :
# TODO: the difference is that = is an assignment operator used to assign a value to a variable, while == is a comparison operator used to check if two values are equal.


# TASK 5
age = 16
has_ticket = True
is_vip = False
# My prediction for can_enter: False
# TODO: can_enter = False
# TODO: print(can_enter)
age = 20
print(can_enter)
# TODO: recompute can_enter and print it again
can_enter = (age >= 18 and has_ticket) or is_vip
print(can_enter)
# TODO: print(not has_ticket)
print(not has_ticket)
# What does not do?
# TODO:it negates the boolean value of a variable, changing True to False and vice versa.


# ---------------- PART C: ASSIGNMENT OPERATORS ----------------

# TASK 6
balance = 100
# My prediction for the final balance: 240
# TODO: add 50, subtract 30, double it (use +=, -=, *=)
balance += 50
balance -= 30
balance *= 2
# TODO: print(balance)
print(balance)


# ===============================================================
# PART 2: STRINGS
# ===============================================================

# ---------------- PART D: CREATING & COMBINING ----------------

# TASK 7
# TODO: quote = "python is amazing"      (He said, 'Python is amazing!')
# TODO: contraction = "It's not a problem."  (It's not a problem.)
# Which quotes did I need for the contraction, and why?
# TODO:"" because the contraction contains '
# TODO: greeting = "Good" + day (use +), then print it
print("Good" + " day")
# TODO: print a divider of 20 dashes (use *)
print("-" * 20)


# ---------------- PART E: METHODS & F-STRINGS ----------------

# TASK 8
messy_name = "   grace HOPPER   "
# TODO: print(f"[{messy_name}]")
print(f"[{messy_name}]")
# TODO: print after .lstrip(), after .rstrip(), after .strip() (inside brackets)
print(f"[{messy_name.lstrip()}]")
print(f"[{messy_name.rstrip()}]")
print(f"[{messy_name.strip()}]")
# TODO: clean_name = ...
clean_name = messy_name.strip()
# TODO: print clean_name.title(), .upper(), .lower()
print(clean_name.title())
print(clean_name.upper())
print(clean_name.lower())
# TODO: print messy_name again - has it changed? Explain why:
print(f"[{messy_name}]")
# Changed because the .strip() method returns with whitespace removed, but does not modify the original string.

# TASK 9
item = "pencil"
price = 1.5
quantity = 12
# TODO: one f-string with the calculation inside the braces
print(f"The total cost for {quantity} {item}s is ${price * quantity:.2f}.")

# ---------------- PART F: INDEXING & SLICING ----------------

# TASK 10
word = "programming"
# Predictions: ?
# TODO: print the first character
print(word[0])
# TODO: print the last character
print(word[-1])
# TODO: print the first three characters
print(word[0:3])
# TODO: print everything from index 3 to the end
print(word[3:10])
# TODO: print the word reversed
print(word[::-1])
# TODO: print every second character
print(word[::2])


# ===============================================================
# PART 3: PUTTING IT TOGETHER
# ===============================================================

# TASK 11: Student ID Card
raw_first = "  ada "
raw_last = " LOVELACE  "
score_1 = 78
score_2 = 92
score_3 = 85
attendance_percent = 80
# TODO: first_name, last_name
first_name = raw_first.strip()
last_name = raw_last.strip()
# TODO: full_name
full_name = f"{first_name} {last_name}"
# TODO: average_score
average_score = (score_1 + score_2 + score_3) / 3
# TODO: passed
passed = attendance_percent >= 75
# TODO: initials
initials = f"{first_name[0].upper()}{last_name[0].upper()}"
# TODO: username
username = f"{first_name.lower()}_{last_name.lower()}"
# TODO: print the card (divider of 30 "=" made with *)  
print("=" * 30)
print(f"Name: {full_name}")
print(f"Initials: {initials}")
print(f"Username: {username}")
print(f"Average Score: {average_score:.2f}")
print(f"Attendance: {attendance_percent}%")
print(f"Passed: {passed}")
print("=" * 30)
