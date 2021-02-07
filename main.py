import os
import random

#
def  run():
    instructions = ['forward', 'left', 'right', 'reverse']
    try:
        while True:
            f = open("demo.txt", "a")
            f.write((instructions[random.randint(0,3)] +  "(" + str(random.randint(0,15)) + ') \n'))
            f.close()
            os.system("cat demo.txt")

    except KeyboardInterrupt:
        exit




#reading the instructions
def read_instructions():
    instructions = []
    with open('demo.txt', 'r') as filehandle:
        filecontents = filehandle.readlines()

        for line in filecontents:
            current = line[:-1]

            instructions.append(current)

    print(instructions)
    delete= str(input("Whould you like to remove the text file?: 'y' or 'n' "))
    if delete == 'y':
        os.system('rm demo.txt')
    else:
        print('Ok')




#reverse function
def reverse():
    instructions = []
    with open('demo.txt', 'r') as filehandle:
        filecontents = filehandle.readlines()

        for line in filecontents:
            current = line[:-1]

            instructions.append(current) 

        instructions.reverse()
        print(instructions)

run()
read_instructions()
reverse()


   