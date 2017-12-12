#python solution.py <number>
import re
import sys

input_number = int(sys.argv[1])

block_size = 1

location_y = 0
location_x = 0

block_dict = {}
block_dict[(0,0)] = 1
numbers_filled = 1
latest_num = 0

def getNodeVal(xcord, ycord):
    try:
        return block_dict[(xcord, ycord)]
    except:
        return 0

while latest_num <= input_number:
    if(block_size**2 == numbers_filled):
        block_size = block_size + 2

    start_num = ((block_size-2)**2) + 1
    location_y = int(-(block_size-1)/2)
    location_x = int((block_size-1)/2)
    #import pdb; pdb.set_trace()

    #MOVE UP
    for i in range(0,block_size-1):
        location_y = location_y + 1
        node_value = 0
        node_value = node_value + getNodeVal(location_x -1,location_y + 1)
        node_value = node_value + getNodeVal(location_x -1,location_y)
        node_value = node_value + getNodeVal(location_x -1,location_y - 1)
        node_value = node_value + getNodeVal(location_x,location_y-1)
        block_dict[location_x, location_y] = node_value
        latest_num = node_value
        print(f"X: {location_x}, Y: {location_y}, N: {latest_num}, D: UP")
        numbers_filled = numbers_filled + 1

    #MOVE TO THE LEFT
    for i in range(0, block_size-1): #remaining horizontal space
        location_x = location_x - 1
        node_value = 0
        node_value = node_value + getNodeVal(location_x + 1,location_y - 1)
        node_value = node_value + getNodeVal(location_x, location_y - 1)
        node_value = node_value + getNodeVal(location_x -1, location_y - 1)
        node_value = node_value + getNodeVal(location_x + 1,location_y)
        block_dict[location_x, location_y] = node_value
        latest_num = node_value
        print(f"X: {location_x}, Y: {location_y}, N: {latest_num}, D: LEFT")
        numbers_filled = numbers_filled + 1

    #MOVE DOWN
    for i in range (0, block_size-1): #remaining verical space
        location_y = location_y - 1
        node_value = 0
        node_value = node_value + getNodeVal(location_x + 1,location_y + 1)
        node_value = node_value + getNodeVal(location_x + 1, location_y)
        node_value = node_value + getNodeVal(location_x + 1, location_y - 1)
        node_value = node_value + getNodeVal(location_x, location_y + 1)
        block_dict[location_x, location_y] = node_value
        latest_num = node_value
        print(f"X: {location_x}, Y: {location_y}, N: {latest_num}, D: DOWN")
        numbers_filled = numbers_filled + 1

    #MOVE TO THE RIGHT
    for i in range(0, block_size-1): #remaining horizontal space
        location_x = location_x + 1
        node_value = 0
        node_value = node_value + getNodeVal(location_x - 1,location_y + 1)
        node_value = node_value + getNodeVal(location_x, location_y + 1)
        node_value = node_value + getNodeVal(location_x + 1, location_y + 1)
        node_value = node_value + getNodeVal(location_x - 1, location_y)
        block_dict[location_x, location_y] = node_value
        latest_num = node_value
        print(f"X: {location_x}, Y: {location_y}, N: {latest_num}, D: RIGHT")
        numbers_filled = numbers_filled + 1

print("----------------")
