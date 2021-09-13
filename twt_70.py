B='ABCDEFGHIJKLMNOPQRSTUVWXYZ';B+=B.lower()+'0123456789+/=';V=0
for _ in'_'*int(input()):
 for c in(Q:=input()):V=V*64+B.index(c)
 while V:_=chr(V%256)+_;V>>=8
 print(_[:~Q.count('=')])

# # without golfing
# char_map = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'+'='
# # see that we are using a 65 char length string to decode 64 char long map (*)
# for _ in range(int(input())):
#     text_in = input()
#     text_out = "_"  # add 1 char for extra padding
#     temp_value = 0
#     for char in text_in:
#         # we are using python big-int for decoding
#         # python can use arbitrary long integers as long as we have available memory
#         # shift the value by 6, same would be temp_value = temp_value << 6
#         temp_value = temp_value * 64
#         # then adding the 6-bit value resolved by the char map
#         temp_value = temp_value + char_map(char)
#         # you see when the char is = its actually not 6 bit but 7:  1 000 000
#         # but actually that will not affect us at all
#     # as soon as we constructed our big integer, we can decode by shifting back 8 bits at a time
#     while temp_value > 0:
#         # we decode the chars in the reverse order
#         temp_char = temp_value % 256 # or temp_value & 0b11111111
#         # and prepending the output
#         text_out = temp_char + text_out
#         # and shifting the int back by 8 bits
#         temp_value = temp_value >> 8
#     # when we finished we need to trim the 'extra' padding chars
#     chars_to_trim = 1 + text_in.count("=")
#     text_out = text_out[:-chars_to_trim]
#     print(text_out)

# (*) explanation for padding
# when chars encoded in Base 64 you'll see the compositon like this
# input  |            |             |           |          |
#        | 0 1 2 3 4 5|0 1|2 3 4 5 0|1 2 3|4 5 0|1 2 3 4 5 |
# output |                |               |                |
#        | 0 1 2 3 4 5 6 7|0 1 2 3 4 5 6 7|0 1 2 3 4 5 6 7 |
#
#
# when 1 missing byte needs to be padded from ascii, you need one '='
# input  |            |             |          x|     =    |
#        | 0 1 2 3 4 5|0 1|2 3 4 5 0|1 2 3|4 5 0|1 2 3 4 5 |
# output |                |               |    missing     |
#        | 0 1 2 3 4 5 6 7|0 1 2 3 4 5 6 7|0 1 2 3 4 5 6 7 |
# even if you poison the previous (adding 1 to the last bit) 6-bit area (marked with x),
# it will not affect the output, as last 3 bits from the previous section
# is not used for decoding and the value assigned to that bit originally was 0 anyway
#
#
# same goes when 2 missing bytes need to be padded from ascii, you need 2 '='
# input  |            |            x|     =    x|     =    |
#        | 0 1 2 3 4 5|0 1|2 3 4 5 0|1 2 3|4 5 0|1 2 3 4 5 |
# output |                |    missing    |    missing     |
#        | 0 1 2 3 4 5 6 7|0 1 2 3 4 5 6 7|0 1 2 3 4 5 6 7 |
# you see that here we poison even two bits (marked with x), but it will not affect the output,
# as only the upper two bits are used from the second 6-bit section
# (the rest of the bits would normally be 0)
