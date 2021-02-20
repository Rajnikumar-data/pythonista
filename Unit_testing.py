# unit_testing

# Simple function

def upper_name(name):
    return name.upper()

print(upper_name("Rajni")

# Same function for testing

def upper_name(name):
    return name.upper()
    
if upper_name("Rajni") == "RAJNI":
    print('pass')
else:
    print('fail')
    
