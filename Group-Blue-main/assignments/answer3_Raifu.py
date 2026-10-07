# TASK 1

# 17 / 5 -> 3.4
# 17 // 5 -> 3
# 17 % 5 -> 2
# 2 ** 5 -> 32
# 7 + 3 * 2 -> 13
# (7 + 3) * 2 -> 20

print(17 / 5)
print(17 // 5) 
print(17 % 5)     
print(2 ** 5)   
print(7 + 3 * 2)
print((7 + 3) * 2)         

# /gives th result in float,  //gives result in int, % gives result int
print(type(10/2))

# TASK 2
movie_minutes = 135
hours = 2
minutes_left = 15
print(f"{hours}:{minutes_left}:00")

# TASK 3
print(48 % 2 == 0)
print(37 % 2 == 0)

# TASK 4
x = 15
y = 20
print(x>y, x<y, x==y, x!=y, x>=15, y<=19)
#(=) is used for assignment. (==) is used for comparison

# TASK 5
age = 16
has_ticket = True
is_vip = False
#My prediction for can enter: False
can_enter = age >= 18 and has_ticket == True or is_vip == True
print(can_enter)
age = 20
can_enter = age >= 18 and has_ticket == True or is_vip == True
print(can_enter)

print(not has_ticket)
#"not" return the opposite value the original bool

# TASK 6
balance = 100
balance += 50
balance -= 30
balance *= 2
print(balance)

# TASK 7
quote = ("He said, 'Python is amazing!'")
contraction = ("It's not a problem.")


greeting = "Good" + " " + "day."
print(greeting)
print("-"*20)

# TASK 8
messy_name = " grace HOOPER "
print(f"[{messy_name}]")
messy_name = messy_name.lstrip()
print(f"[{messy_name}]")
messy_name = messy_name.rstrip()
print(f"[{messy_name}]")
messy_name = messy_name.strip()
print(f"[{messy_name}]")
clean_name = "harry potter"
print(clean_name.title())
print(clean_name.upper())
print(clean_name.lower())

# TASK 9
item = "pencil"
price = 1.5
quantity = 12

# TASK 10
word = "programming"
print(word[0])
print(word[-1])
print(word[0:3])
print(word[3:])
print(word[::-1])
print(word[::2])

# TASK 11
#no time
