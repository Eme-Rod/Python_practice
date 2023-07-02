import sys
import time

pattern_char = '*'
pattern_size = 5
count = 1
str_to_print = pattern_char * pattern_size

try:
    while True:
        while count < pattern_size:
            print(' ' * count + str_to_print)
            count += 1
            time.sleep(0.03)
        while count >= 0:
            print(' ' * count + str_to_print)
            count -= 1
            time.sleep(0.03)
except KeyboardInterrupt:
    sys.exit()
