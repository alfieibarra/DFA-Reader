import sys
import re

def main():

    if len(sys.argv) < 1:
        print("Usage: Enter filename in command prompt")

    command_arg = sys.argv[1]

    try:
        file = open(command_arg, 'r')

        #read num_states first
        file.readline()

        alphabet = file.readline()
        
        dictionary = {}

        while True:
            line = file.readline()
            if (len(line) == 2):
                start_state = line
                break
            line = line.replace('\'', '')
            line = line.replace('\n', '')
            line_ar = line.split(' ')
            concat = line_ar[0] + '-' + line_ar[1]
            dictionary[concat] = line_ar[2]

        accept_states = file.readline()

        for line in file:
            state = start_state
            for c in line:
                if c in alphabet:
                    #Do not read end of line char
                    if c == '\n':
                        break
                    state += '-' + c
                    state = state.replace('\n', '')
                    state = dictionary[state]
            #If no inputs
            state = state.replace('\n', '')
            if state in accept_states:
                print ("Accept")
            else:
                print ("Reject")  
        file.close()

    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
        sys.exit

main()