# unit_testing

# Simple function

def upper_name(name):
    return name.upper()

print(upper_name("Rajni"))

# Same function for testing

def upper_name(name):
    return name.upper()
    
if upper_name("Rajni") == "RAJNI":
    print('pass')
else:
    print('fail')
    
    
### Easy Testing

def upper_name(name):
    return name.upper()

# In the above example data type(string) is required to perform the correct function. 
# Therefore is string is the input then the test should behave correctly.
 # easy Test
if upper_name("Rajni") == "RAJNI":
    print('pass')
else:
    print('fail')
 