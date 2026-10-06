# TASK 1
task1_answers = ["student_name, totalprice, _count, Score, class, user-age, max_value_1"]
# Python's naming rule stated that a variable name must not start with a number.

# TASK 2
exam_score = 87
student_age = 20
total_price = 150

# TASK 3
city_population = 2500000
temperature = 23.6
is_raining = True
middle_name = None
school_name = "TODO nusery and primary school"
print(city_population, type(city_population))
print(temperature, type(temperature))
print(is_raining, type(is_raining))
print(middle_name, type(middle_name))
print(school_name, type(school_name))

# TASK 4
a = 10
b = a
a = 20
# My prediction: a = 20, b = 10
print(a, b)
# Explanation: 'b' was assigned to the 'a' that was above it, so 'b' was no more involved in the reassignment of 'a'.

# TASK 5
task5_predictions = ["1. int, 2. float, 3. float, 4. bool, 5. str, 6.Nonetype"]
print(type(7))
print(type(7.0))
print(type(7 + 2.5))
print(type(True))
print(type("7"))
print(type(None))

# TASK 6
level = 1
Level = 2
LEVEL = 3
# My prediction : 6
print(level + Level + LEVEL)
# Python is case-sensitive

# TASK 7
quantity_text = "12"
unit_price_text = "4.50"

quantity = int(quantity_text)
unit_price = float(unit_price_text)
total_cost = quantity * unit_price
print(total_cost, type(total_cost))
# Total cost is a float because most operation done in python returns a float
total_cost_text = str(total_cost)
print(total_cost_text, type(total_cost_text))

# TASK 8
#print(int("apple"))
#ValueError: invalid literal for int() with base 10: 'apple'

# "25" has the literal of an int while "apple" does not
#int(3.9) gives: 3 (truncate)
#int(-3.9) gives: -3 (truncate)
#float(5) gives: 5.0

# TASK 9
item_name = "Notebook"
price_text = "2.75"
quantity_text_9 = "4"
discount_percent = 10
is_member = True

subtotal = float(price_text) * int(quantity_text_9)
discount_amount = subtotal * (discount_percent/100)
final_total = discount_amount + subtotal
print(subtotal)
print(discount_amount)
print(final_total)
print(is_member, type(is_member))
