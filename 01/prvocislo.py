from math import sqrt
import sys

# one of larger prime numbers is f.e. 10657331232548839
user_num = int(sys.argv[1])

# parity check
if user_num%2 ==0 and user_num>2 or user_num==1:				
    print(f"Číslo {user_num} není prvočíslo.")
# algorithm for odd numbers    
else:
    for i in range(3,round(sqrt(user_num))+1,2):
        if user_num%i ==0:
            print(f"Číslo {user_num} není prvočíslo.")
            break
    else:
        print(f"Číslo {user_num} je prvočíslo.")
    