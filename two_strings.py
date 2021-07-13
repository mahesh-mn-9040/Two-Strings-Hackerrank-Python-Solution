import math
import os
import random
import re
import sys

#here the soluti0n starts:

def twoStrings(s1, s2):
    for i in s1:  #we iterate through in s1
        if i in s2:   #we check if i present in s2
            return "YES"
            break
    else:
        return "NO"
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
