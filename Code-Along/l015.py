try:
    my_int = int(input("input an integer ")) 
except ValueError:
    print("Value error, my int must be an integer.")
else: 
    print(f"my_int = {my_int}")  
    
#när man försöker anropa en variable eller string som
# inte finns så är det en typ av runtim error
#syntax error du har skrivit något fel.
# runtime error när något inte fungerar som det ska inom sparning 
# av minnet/value error
