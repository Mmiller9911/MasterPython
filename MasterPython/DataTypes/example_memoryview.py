
#  Explanation how we modify internal data in above program :
#  Here, we updated the memory view’s 2nd index to ASCII value as 74 (J).
#  In this memory view object mem_view references the same buffer or memory and updating the index in mem_view and it also updates byte_array.


# random bytearray
byte_array = bytearray('XYZ', 'utf-8')
print('Before update:', byte_array)

mem_view = memoryview(byte_array)

# update 2nd index of mem_view to J
mem_view[2] = 74
print('After update:', byte_array)