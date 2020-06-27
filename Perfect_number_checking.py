# Python program to check perfect number

# function definition for perfect

def perfect(n):
    
    s=0
    
    for i in range(1,n+1 // 2): # n+1 is to count the last number also
        
        if n % i ==0:
            s = s + i
    return(s)

# function definition to check perfect number
    
def check_perfect():
    
    x = int(input("Enter the number to check perfect number : "))
    
    if x == perfect(x):
        
        print(x,"is a perfect number.\n")
        
    else:
        
        print(x,"is not a perfect number.")

# function call
        
check_perfect()
