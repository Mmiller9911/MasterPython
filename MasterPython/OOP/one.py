# file one.py
def func():
    print("func() in one.py")
    print("the current name is now: {}".format(__name__))

print("top-level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")

i = 1
while i < 10:
  print("i is {} and still less than 10".format(i))
  i += 1
else:
  print("i is no longer less than 10 because it is 10")

print(globals())