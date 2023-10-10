# Multiply
def mul(num1, num2):
       value = float(num1 * num2)
       return value
   
# Addition 
def add(num1, num2):
       value = float(num1 + num2)
       return value
  
# Subtract
def sub(num1, num2):
       value = float(num1 - num2)
       return value

# Divide  
def div(num1, num2):
       value = float(num1 / num2)
       return value
    
       
 # Operation Caller (3)   
def operation(ope, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    if ope.upper() == 'A':
        ans = add(num1, num2)
        return ans
    elif ope.upper() == 'B':
        ans = sub(num1, num2)
        return ans
    elif ope.upper() == 'C':
        ans = mul(num1, num2)
        return ans
    elif ope.upper() == 'D':
        try:
            ans = div(num1, num2)
            return ans
        except:
            print("You can't divide with zero! ")
        
        
        
# Start point (1)
def start():      
    num1 = input('First Number: ')
    num2 = input('Second Number: ')
    op = input('Which operation do you want: ' + '\n[a] Addition ' + '\n[b] Subtraction ' + '\n[c] Multiplication ' + '\n[d] Division ' + '\nType the option a/b/c/d: ')
    check(num1, num2, op)
  
  
  
# Check for invalid input (2)
def check(num1, num2, op):
    if num1 in "1234567890" and num2 in "1234567890":
                 if op.upper() in "ABCD":
                       print('\n' + str(operation(op, num1, num2))) 
                 else:
                   print('\n\n [ERROR] Invalid Input in the operation\n')                
    else:
         print('\n\n [ERROR] Invalid Input in the Number\n')
    print('\n__________________________\nTry Again\n__________________________\n\n')
    start()     
           
   
   
# Ultimate Start Point
start()
    

