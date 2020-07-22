#  ============================================================================================================================================
#  Bytearrays
#  Since a byte is immutable we must use a bytearray to modify the data
#  ============================================================================================================================================

mutable_bytes = bytearray()  # bytearray(b'') - empty array
print(mutable_bytes)
print(type(mutable_bytes))

mutable_bytes = bytearray(3)  # bytearray(b'\x00\x00\x00')
print(mutable_bytes)
print(type(mutable_bytes))

mutable_bytes = bytearray(b'\xBE\xEF')  #  bytearray(b'\xbe\xef') create with hex
print(mutable_bytes)
print(type(mutable_bytes))
mutable_bytes[0] = 0
print(mutable_bytes)
mutable_bytes.append(255) # 255 is the max value of bytes
print(mutable_bytes[0:1])