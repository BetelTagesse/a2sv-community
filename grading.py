#!/bin/python

import math
import os
import random
import re
import sys


def gradingStudents(grades):
      for i in range(len(grades)):
        if grades[i] > 37:
            if grades[i]%5 >= 3:
                grades[i] = int(math.ceil(grades[i] / 5) *5 + 5)
        else:
            return grades
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(raw_input().strip())

    grades = []

    for _ in xrange(grades_count):
        grades_item = int(raw_input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
