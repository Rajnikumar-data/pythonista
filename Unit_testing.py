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
    
    
### Levels of Testing with given example
# Function
def upper_name(name):
    return name.upper()

# for easy testing: In the above example data type(string) is required to perform the correct function. 
# Therefore if string is the input then the test should behave correctly otherwise crash.


 
# For Medium testing: In the above example data type(string) is required to perform the correct function. 
# if integer/boolean is the input then the test should still given the right output that is in this case it will crash.


##Hard testing: any kind of input that may hack the function and effect the programme, user is guided immediately.



