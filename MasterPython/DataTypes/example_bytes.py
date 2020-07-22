#  ============================================================================================================================================
#  Bytes
#  Bytes are immutable
#  Bytes objects can be constructed the constructor, bytes(), and from literals;
#  use a b prefix with normal string syntax: b'python'. To construct byte arrays, use the bytearray() function.
#  A byte is made up of 8 bits, a single 0/1 value
#  ============================================================================================================================================

# bytesliteral   ::=  bytesprefix(shortbytes | longbytes)
# bytesprefix    ::=  "b" | "B" | "br" | "Br" | "bR" | "BR"
# shortbytes     ::=  "'" shortbytesitem* "'" | '"' shortbytesitem* '"'
# longbytes      ::=  "'''" longbytesitem* "'''" | '"""' longbytesitem* '"""'
# shortbytesitem ::=  shortbyteschar | bytesescapeseq
# longbytesitem  ::=  longbyteschar | bytesescapeseq
# shortbyteschar ::=  <any ASCII character except "\" or newline or the quote>
# longbyteschar  ::=  <any ASCII character except "\">
# bytesescapeseq ::=  "\" <any ASCII character>

# x = b"Bytes objects are immutable sequences of single bytes"
# print(x)
#
# #created from a iterable of ints, string, bytes or buffer objects.
# x = bytes('Python, bytes', 'utf8')
# print(x)
#
# x = b'El ni\xc3\xb1o come camar\xc3\xb3n'
# print(x)
# s = x.decode()
# print(type(s))
# print(s)
#
# #create a bytes object encoded using 'cp855'
# x = b'\xd8\xe1\xb7\xeb\xa8\xe5 \xd2\xb7\xe1'
# print(x)
# #return a string using decode 'cp855'
# y = x.decode('cp855')
# print(y)

empty_bytes = bytes(4)  # 4 bytes aka 32 bits of information
print(empty_bytes)      # b'\x00\x00\x00\x00'
print(type(empty_bytes))

# hexadecimal notation
data_bytes = bytes(b'\xFF\xFF')
print(data_bytes)

