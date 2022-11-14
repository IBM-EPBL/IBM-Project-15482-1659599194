'''
It verify the entered details is valid
'''
import re 
# re: means regular expression.. used for verify valid emai id 
       
def checkValid(name,email,password):
        error=None
        if name == "":
            error="Username cannot be blank."
        elif len(name) <=2:
            error="Username must be between 3 and 30 characters" 
        if len(password) <6:
            error="Password should contains atleast 6 characters"
        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(pat,email):
            print("Valid Email")
        else:
            error="Email is not valid."
        return error
