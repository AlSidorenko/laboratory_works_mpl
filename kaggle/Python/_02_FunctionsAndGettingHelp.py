# In[1]:
# print("In[1]:")
# help(round)

# In[2]:
#print("In[2]:")
# help(round(-2.01))

# In[4]:
print("In[4]:")
def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

# min = least_difference(5, 7, -23)
# print("Result min: ", min, "\n")

# In[5]:
print("In[5]:")
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), "\n"
    # Python allows trailing commas in argument lists. How nice is that?
)

# In[6]:
# print("In[6]:")
# help(least_difference)

# In[7]:
print("In[7]:")
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.

    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

# In[8]:
# print("In[8]:")
# help(least_difference)

# In[09]
print("In[9]:")
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)

# In[10]:
print("In[10]:")
mystery = print()
print(mystery, "\n")

# In[11]:
print("In[11]:")
print(1, 2, 3, sep=' < ')
print()

# In[12]:
print("In[12]:")
print(1, 2, 3)
print()

# In[13]:
print("In[13]:")
def greet(who="Colin"):
    print("Hello,", who)

greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")
print()

# In[14]:
print("In[14]:")
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n', # '\n' is the newline character - it starts a new line
)
print()

# In[15]:
print("In[15]:")
def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)