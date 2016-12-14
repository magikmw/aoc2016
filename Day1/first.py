#!/bin/env python3

# Split input into tuples - direction and number, iterate on list
# Direction variable updates according to instruction (N = y++, S = y--, E = x++, W = x--)
# Let starting position be 0,0
# After iteration on instructions calculate distance from current to 0,0

import math

final_input = "L3, R2, L5, R1, L1, L2, L2, R1, R5, R1, L1, L2, R2, R4, L4, L3, L3, R5, L1, R3, L5, L2, R4, L5, R4, R2, L2, L1, R1, L3, L3, R2, R1, L4, L1, L1, R4, R5, R1, L2, L1, R188, R4, L3, R54, L4, R4, R74, R2, L4, R185, R1, R3, R5, L2, L3, R1, L1, L3, R3, R2, L3, L4, R1, L3, L5, L2, R2, L1, R2, R1, L4, R5, R4, L5, L5, L4, R5, R4, L5, L3, R4, R1, L5, L4, L3, R5, L5, L2, L4, R4, R4, R2, L1, L3, L2, R5, R4, L5, R1, R2, R5, L2, R4, R5, L2, L3, R3, L4, R3, L2, R1, R4, L5, R1, L5, L3, R4, L2, L2, L5, L5, R5, R2, L5, R1, L3, L2, L2, R3, L3, L4, R2, R3, L1, R2, L5, L3, R4, L4, R4, R3, L3, R1, L3, R5, L5, R1, R5, R3, L1"

test_a_input = "R2, R2, R2"
test_a_output = 2

test_b_input = "R5, L5, R5, R3"
test_b_output = 12

input = final_input
direction = "N"
location = {"x": 0, "y": 0}

def cdirection(cur, turn):
    if cur == "N" and turn == "R": return "E"
    if cur == "N" and turn == "L": return "W"
    if cur == "E" and turn == "R": return "S"
    if cur == "E" and turn == "L": return "N"
    if cur == "S" and turn == "R": return "W"
    if cur == "S" and turn == "L": return "E"
    if cur == "W" and turn == "R": return "N"
    if cur == "W" and turn == "L": return "S"

def move(dir, dist, location):
    if dir == "N": location["y"] += dist
    if dir == "S": location["y"] -= dist
    if dir == "E": location["x"] += dist
    if dir == "W": location["x"] -= dist

    return location

in_list = input.replace(" ","").split(",")
for pair in in_list:
    print(pair[0] + "|" + pair[1:])

    direction = cdirection(direction, pair[0])
    location = move(direction, int(pair[1:]), location)
    print(location)

#result = math.sqrt((0 - location["x"])**2 + (0 - location["y"])**2)
result = math.fabs(location["x"]) + math.fabs(location["y"])
print(int(result))
