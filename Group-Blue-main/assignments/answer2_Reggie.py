# My predictions (BEFORE running):
#   17 / 5       = 3.4
#   17 // 5      = 3
#   17 % 5       = 1
#   2 ** 5       = 32
#   7 + 3 * 2    = 13
#   (7 + 3) * 2  = 20

print(17 / 5)       
print(17 // 5)      
print(17 % 5)     
print(2 ** 5)      
print(7 + 3 * 2)    
print((7 + 3) * 2)

# / gives the divived value as a float, // gives the whole number ofthe result, % gives the remainder of the result

movie_minutes = 135
hours = 135 // 60
minutes_left = 135 % 60
print(f"{movie_minutes} is {hours} hours and {minutes_left} minutes.")

is_even = 48 % 2 == 0
is_odd = 37 % 2 == 0
print(is_even)
print(is_odd)
# because even numbers are numbers that are divisible by 2 without remainder while odd numbers are the direct opposite

x = 15
y = 20
print(x > y)
print( x < y)
print(x == y)
print(x != y)
print(x >= 15)
print(y <= 19)
# difference between = and ==: = is an assignment operator while == is a comparison operator

age = 16
has_ticket = True
is_vip = False
# my prediction for can_enter = false
can_enter = has_ticket and (age == 18 or is_vip)
print(can_enter)

age = 20 
can_enter = has_ticket and (age >= 18 or is_vip)
print(can_enter)
print(not has_ticket)


balance = 100 
# my prediction for final balance = 240
balance += 50
balance -= 30
balance *= 2
print(balance)


quote = "He said 'python is amazing!'"
print(quote)
contraction = "It's not a problem."
print(contraction) # i used "" because the string contains a single quote and using a single qoute would confuse python on where the string ends.
print("Good" + " " + "morning" + "!")
print("-" * 20)


messy_name = "  grace HOPPER  "
print(f"{messy_name}")
print(messy_name.lstrip())
print(messy_name.lstrip().rstrip())
print(messy_name.strip())
clean_name = messy_name.strip()
print(clean_name.title())
print(clean_name.upper())
print(clean_name.lower())
print(messy_name)
# it doesn't change because messy_name the string stored in messy_name didnt change.

item = "pencil"
price =1.5
quantity = 12
print(f"{quantity} {item}(s) cost {price * quantity} in total")

