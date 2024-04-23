def input_int(prompt):
   
    while True:
       try:
          return int(input(prompt))
       except ValueError:
          print("Value error, my int must be an integer.")

age = input_int("input age")
length = input_int("input length")
weight = input_int("input weight")
print(f"age = {age}, length = {length}, weight = {weight}")
   