#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
   try:
       num = int(sys.argv[1])
   except ValueError:
       print(f"Error: Argument '{sys.argv[1]}' is not a valid arguement.")
       sys.exit(1)
else:
   num = 0

print(f"---Checking value {num} ---")

if num > 10:
   print("Value is greater than 10.")
else:
   print("Value is less than 10.")

if num < 0:
   print("Value is negative.")
elif num == 0:
   print("Value is exactly Zero.")
elif num > 0 and num <=50:
   print("Value is Greater than Zero and less than or equal to 50.")
else:
   print("Value is greater than 50.")

is_ready = (num % 2 == 0)

if is_ready:
   print("The value is ready.(Even)")
else:
   print("The value is not ready.(Odd)")


