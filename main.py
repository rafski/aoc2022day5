import numpy
import re

moves = []
with open('moves.txt') as f:
    input = f.read().splitlines()
    moves_text = numpy.array(input)
    #print(moves_text[0])
    for move in moves_text:
        move = re.sub(r'[^0-9]', ' ', move)
        move = move.split()
        move = list(map(int, move))
        moves.append(move)
        #print(move)
    #print(moves[5][0])

stack1 = numpy.array(["W", "L", "S"])
stack2 = numpy.array(["Q", "N", "T", "J"])
stack3 = numpy.array(["J", "F", "H", "C", "S"])
stack4 = numpy.array(["B", "G", "N", "W", "M", "R", "T"])
stack5 = numpy.array(["B", "Q", "H", "D", "S", "L", "R", "T"])
stack6 = numpy.array(["L", "R", "H", "F", "V", "B", "J", "M"])
stack7 = numpy.array(["M", "J", "N", "R", "W", "D"])
stack8 = numpy.array(["J", "D", "N", "H", "F", "T", "Z", "B"])
stack9 = numpy.array(["T", "F", "B", "N", "Q", "L", "H"])
#print(stack9[2])
stacks = numpy.array([stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9], dtype=object)
#print(stacks[8][2])

"""
for move in moves:
    from_stack = stacks[move[1] - 1]
    to_stack = stacks[move[2] - 1]
    for n in range(0, move[0]):
        print("from stack: ", move[1] , from_stack)
        print("to stack: ", move[2], to_stack)
        to_stack = numpy.insert(to_stack, 0, from_stack[0])
        print("to stack: ", move[2], to_stack)
        from_stack = numpy.delete(from_stack, 0)
        print("from stack: ", move[1], from_stack)
        n += 1
        print(n)
    stacks[move[1] - 1] = from_stack
    stacks[move[2] - 1] = to_stack


for stack in stacks:
    print(stack[0])
"""
for move in moves:
    from_stack = stacks[move[1] - 1]
    to_stack = stacks[move[2] - 1]
    for n in range(move[0]-1, -1, -1):
        print("from stack: ", move[1] , from_stack)
        print("to stack: ", move[2], to_stack)
        to_stack = numpy.insert(to_stack, 0, from_stack[n])
        print("to stack: ", move[2], to_stack)
        from_stack = numpy.delete(from_stack, n)
        print("from stack: ", move[1], from_stack)
        n += 1
        print(n)
    stacks[move[1] - 1] = from_stack
    stacks[move[2] - 1] = to_stack

for stack in stacks:
    print(stack[0])