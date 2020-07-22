# All functions return something even if it is none
# parameter is the variable defined in a method and argument is the actual value passed to the method
# the parameters which are passed into a method are known as the methods "signature", so if two methods have the same params they have the same signature
# Wherever possible try to write functions which use local variables + parameters - only access global and nonlocal values when it is ABSOLUTELY necessary


def python_food():
    print('chicken vindaloo')


def centretext(*args, sep='(*)'):
  #  text = str(text)
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    # print(' ' * left_margin, text, end=end, file=file, flush=flush)
    return ' ' * left_margin + text

# python_food()
# print(python_food())
# with open ('centred', mode='w') as centred_file:
#     centretext('566', file=centred_file)
#     centretext('wtf', 'daaawwwg', 8, 'wtf wtf wtf wtf wtf wtf wtf wtf',sep='^',file=centred_file)

# with open ('centred', mode='w') as centred_file:
print(centretext('566'))
print(centretext('wtf', 'daaawwwg', 8, 'wtf wtf wtf wtf wtf wtf wtf wtf',sep='^'))

#  ============================================================================================================================================
# Reduce takes a function and a sequence and reduces the sequence to a single value after repeatedly calling the function
# very unlikely to be used
import timeit
import functools

# each time round the values used are the result and the next number in the list


def calc_values(x, y: int):
    return x + y


numbers = [2, 3, 5, 8, 13]
reduced_value = functools.reduce(calc_values, numbers)
print(reduced_value)
print(sum(numbers))
result = calc_values(2, 3)
result = calc_values(result, 5)
result = calc_values(result, 8)
result = calc_values(result, 13)
print(result)
#  ============================================================================================================================================
