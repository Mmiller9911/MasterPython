segment = 1                                  #there should always be at least one segment
segment_length = 0                           #initilize the length at 0
ipaddress = input('enter an ipaddress!')
if ipaddress [-1] != '.':                   #if the address doesnt end with a period then add one
    ipaddress += '.'

for character in ipaddress:                 #for every character in the string
    if character == '.':                    #if the character is a period
        print ('segment {} contains {}'.format(segment,segment_length))  #the segment has finished processing so print the number of the segment and the current number of characters
        segment += 1                    #as the segment has completed up the segment number to the next one
        segment_length = 0              #as a new segment is started then set its length back to 0
    else:
        segment_length +=1              #if the character is not a period then add the value to the number of characters in the section

#192.168.1.1   = 3,3,1,1
#192.168.1.1.  = 3,3,1,1
#.192.168.1.1. = 0,3,3,1,1
#.192.168.1.1  = 0,3,3,1,1