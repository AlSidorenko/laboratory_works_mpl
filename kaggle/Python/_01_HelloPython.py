spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)
print()

#  "True division" is basically what your calculator does:
print(5 / 2)
print(6 / 2)
print()

# The // operator gives us a result that's rounded down to the next integer.
print(5 // 2)
print(6 // 2)
print()

hat_height_cm = 25
my_height_cm = 190
# How tall am I, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")
print()

total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)
print()

print(min(1, 2, 3))
print(max(1, 2, 3))
print()

print(abs(32))
print(abs(-32))
print()

print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)
print()

# If you're curious, these are examples of lists. We'll talk about
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
a = [1, 2, 3]
b = [3, 2, 1]

a, b = b, a

print(a)
print(b, "\n")
