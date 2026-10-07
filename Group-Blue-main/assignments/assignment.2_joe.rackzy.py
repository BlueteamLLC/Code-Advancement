
# Part A: Naming Rules
task1_answer = ["student_name","price_count","Score", "max_value"]
#the reason why "class"is invaild is because it is keyword in python
 
exam_score = 57
student_age = 19
total_price = 54.4
# Part B: Creating Variables
city_population = 1_250_000
temperature = -3.5
is_it_raining = False
middle_name = None
school_name = "Emmanuel's"
print(city_population,type(city_population))
print(temperature,type(temperature))
print(is_it_raining,type(is_it_raining))
print(middle_name,type(middle_name))
print(school_name,type(school_name))
a = 10
b = a
a = 20
# When 'b = a' ran, 'b' was attached to the value '10' that 'a' was pointing to.
# Changing 'a' to point to '20' did not alter 'b', because 'b' remains a label
# pointing to the value '10'.
print(a, b)

# 1. type(7)       -> "int"
# 2. type(7.0)     -> "float"
# 3. type(7 + 2.5) -> "float"
# 4. type(True)    -> "bool"
# 5. type("7")     -> "str"
# 6. type(None)    -> "NoneType"

task5_predictions = ["int", "float", "float", "bool", "str", "NoneType"]

print(type(7))
print(type(7.0))
print(type(7 + 2.5))
print(type(True))
print(type("7"))
print(type(None))
# Adding an int and a float resulting in a float (7 + 2.5) was clear, but type(None)
# returning 'NoneType' is worth noting because it has its own unique type class.
level = 1
Level = 2
LEVEL = 3
print(level + Level + LEVEL)
#'level', 'Level', and 'LEVEL' are three completely different variables
# distinct variables stored in separate memory spaces and the will have different 
# so the answer is 6 because 1 + 2 + 3 = 6.
  
quantity_text = "12"
unit_price_text = "4.50"

quantity_text = int(quantity_text)
unit_price_text = float(unit_price_text)
total_cost =quantity_text * unit_price_text
print(type(total_cost))
# Multiplying an 'int' by a 'float' performs an implicit conversion, resulting in a 'float'.
total_cost = str(total_cost)
print(total_cost,type(total_cost))

# int("apple")It tells us that the value passed to int() is invalid because "apple" cannot be parsed as a base-10 integer.


# int("25") works because the string contains digits that can be converted into an integer, whereas "apple" consists of alphabetic characters with no numeric value.
#REPL Checks:
# - int(3.9) gives 3. It truncates (discards the fractional part rather than rounding).
# - int(-3.9) gives -3.
# - float(5) gives 5.0.
item_name = "Notebook"
price_text = "2.75"
quantity_text_9 = "4"
discount_percent = 10 
is_member = True
#convertiont of string   to a float and a string to an int
price = float(price_text)
quantity = int(quantity_text_9)
subtotal = price * quantity
discount_amount = subtotal *discount_percent / 100
final_total = subtotal - discount_amount
print("item name: ",item_name)
print("subtotal: ",subtotal)
print("discount amount:",discount_amount)
print("final total:",final_total)


print("is member: ",type(is_member))




