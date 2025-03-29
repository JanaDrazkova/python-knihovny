from math import sqrt
import sys

# one of larger prime numbers is f.e. 10657331232548839

def is_prime_number(num):
    if num%2 ==0 and num>2 or num==1:				
       return False
    # algorithm for odd numbers    
    else:
        for i in range(3,round(sqrt(user_num))+1,2):
            if user_num%i ==0:
               return False
        return True
    

try:
    user_num = int(sys.argv[1])
except ValueError:
    print(f"Zadané číslo musí být přirozené.")
    exit()

#non_positive integers
if user_num < 1:
    raise ValueError(f"Zadané číslo musí být přirozené.")

# parity check
if is_prime_number(user_num):
    print(f'{user_num} je prvočíslo.')
else:
    print(f'{user_num} není prvočíslo.')
    