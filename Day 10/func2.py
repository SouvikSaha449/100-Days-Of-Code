
#Output with functions

name=""
def format_name(fname,lname):
    #docstrings:- Where we can write a documentation for a function and what inputs should be taken and what the output will be
    """This function takes the first name and last name of a person and returns the full name of the person in title case"""
    Fname = fname.title()
    Lname = lname.title()
    return Fname+ " "+Lname

name=format_name("john","doe")
print(name)
