
print(17 / 5)
print(17 // 5)
print(17 % 5)
print(2 ** 5)
print(7 + 3 * 2)
print((7 + 3) * 2)

print(type(10 / 2)) 


movie_minutes = 135
hours = movie_minutes // 60
minutes_left = movie_minutes % 60
print(f"{movie_minutes} minutes is {hours} hours and {minutes_left} minutes")


print(48 % 2 == 0)  
print(37 % 2 == 0)  


x = 15
y = 20
print(x > y)    
print(x < y)    
print(x == y)   
print(x != y)   
print(x >= 15)  
print(y <= 19) 



age = 16
has_ticket = True
is_vip = False
can_enter = has_ticket and (age >= 18 or is_vip)
print(can_enter)  
age = 20
can_enter = has_ticket and (age >= 18 or is_vip)
print(can_enter) 
print(not has_ticket)  


balance = 100

balance += 50
balance -= 30
balance *= 2
print(balance)

quote = "He said, 'Python is amazing!'"
print(quote)
contraction = "It's not a problem."
print(contraction)


greeting = "Good" + " " + "morning" + "!"
print(greeting)
print("-" * 20)


messy_name = "   grace HOPPER   "
print(f"[{messy_name}]")
print(f"[{messy_name.lstrip()}]")
print(f"[{messy_name.rstrip()}]")
print(f"[{messy_name.strip()}]")
clean_name = messy_name.strip()
print(clean_name.title())
print(clean_name.upper())
print(clean_name.lower())
print(f"[{messy_name}]")



item = "pencil"
price = 1.5
quantity = 12
print(f"{quantity} {item}(s) cost {price * quantity} in total")


word = "programming"
print(word[0])      
print(word[-1])     
print(word[0:3])    
print(word[3:])     
print(word[::-1])   
print(word[::2])    


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
username = first_name.lower() + last_name.lower()[0:3]

print("=" * 30)
print(f"Name: {full_name}")
print(f"Initials: {initials}")
print(f"Username: {username}")
print(f"Average: {average_score}")
print(f"Passed: {passed}")
print("=" * 30)
