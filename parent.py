
# initialize a variable local_val and set its value to the string "magical unicorns"
local_val = "magical unicorns"

# initialize a function square that takes as a parameter x 
def square(x):

    # it then returns the value of x times x
    return x * x


# initialize a class named User
class User:

    # initialize a method that modifies the python method __init__ and passes in two parameters self and name
    def __init__(self, name):

        # initialize an atribute "name" that takes its value from the parameter "name" passed into the method
        self.name = name

    # initialize a method for the class User called "say_hello" and pass in the parameter self
    def say_hello(self):

        # return the string "hello"
        return "hello"

# print the return of the function square defined above with the argument 5
print(square(5))

# initialize a new object variable called "user" from the User class with the argument "Anna" passed
user = User("Anna")

# print the name attribute of the object user
print(user.name)

# print the return value from the method say_hello() from the User class
print(user.say_hello())

# 1.__name__ is not only automatically created, but is also assigned a value. In your document parent.py add this line:
print(__name__)

# 2. execute parent.py from the command line
# DONE

# 3.You should see __main__ printed to the console
# CORRECT

# 7. In parent.py add the following:
if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)
  

# 8. Now try running the file directly. You should see the file is being executed directly printed in the console.
# CORRECT

