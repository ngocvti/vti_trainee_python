import time, sys

indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.05) # pause screen for 0.1 second

        if indentIncreasing:
            indent += 2
            if indent == 40:
                indentIncreasing = False
        else:
            indent -= 2
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt: # exit program when press Ctrl + C
    sys.exit()
