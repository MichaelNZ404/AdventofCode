#python solution.py <number>
import re
import sys

number = int(sys.argv[1])

block_size = 1
while number > block_size**2:
    block_size = block_size + 2

location_y = 0
location_x = 0

if block_size is not 1:
    start_num = ((block_size-2)**2) + 1
    location_y = int(-(block_size-1)/2) + 1
    location_x = int((block_size-1)/2)
    offset = number-start_num

    #MOVE UP
    if offset > (block_size-2): #remaining vertical space
        location_y = location_y + (block_size-2)
        offset = offset - (block_size-2)
    else:
        location_y = location_y + offset
        offset = 0

    #MOVE TO THE LEFT
    if offset > (block_size-1): #remaining horizontal space
        location_x = location_x - (block_size-1)
        offset = offset - (block_size-1)
    else:
        location_x = location_x - offset
        offset = 0

    #MOVE DOWN
    if offset > (block_size-1): #remaining verical space
        location_y = location_y - (block_size-1)
        offset = offset - (block_size-1)
    else:
        location_y = location_y - offset
        offset = 0

    #MOVE TO THE RIGHT
    if offset > (block_size-1): #remaining horizontal space
        location_x = location_x + (block_size-1)
        offset = offset - (block_size-1)
    else:
        location_y = location_y + offset
        offset = 0

print(abs(location_x) + abs(location_y))
