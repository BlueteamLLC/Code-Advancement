
task1_answers = ["student_name", "_count", "Score", "max_value_1"]

exam_score = 87
student_age = 19
total_price = 149.99


city_population = 1_250_000
temperature = -3.5
is_raining = False
middle_name = None
school_name = "Riverside High"
print(city_population, type(city_population))
print(temperature, type(temperature))
print(is_raining, type(is_raining))
print(middle_name, type(middle_name))
print(school_name, type(school_name))



a = 10
b = a
a = 20

print(a, b)

task5_predictions = [
    "int",  
    "float",  
    "float",  
    "bool",  
    "str", 
    "NoneType", 
]
print(type(7), type(7.0), type(7 + 2.5), type(True), type("7"), type(None))

level = 1
Level = 2
LEVEL = 3

print(level + Level + LEVEL)

quantity_text = "12"
unit_price_text = "4.50"
quantity = int(quantity_text)
unit_price = float(unit_price_text)
total_cost = quantity * unit_price
print(total_cost)
print(type(total_cost))

total_cost_text = str(total_cost)
print(type(total_cost_text))


item_name = "Notebook"
price_text = "2.75"
quantity_text_9 = "4"
discount_percent = 10
is_member = True
price = float(price_text)
quantity_9 = int(quantity_text_9)
subtotal = price * quantity_9
discount_amount = subtotal * discount_percent / 100
final_total = subtotal - discount_amount
print("Item:", item_name)
print("Subtotal:", subtotal)
print("Discount:", discount_amount)
print("Final total:", final_total)
print(is_member, type(is_member))

