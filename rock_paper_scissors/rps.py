#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n <= 0:
    return [[]]

  options = ['rock', 'paper', 'scissors']
  answer = [[""] * n for i in range(len(options)**n)]

  
  #change = 0
  #for i in range(0, len(options)):
  #  for j in range(0, len(options)**(n-1)):   # The amount of times each option should appear in a specified position
  #    answer[j + change][0] = options[i]
  #      #if(len(answer) == 1):
  #      #  answer[i] = options[j]
  #      #else:
  #  change += len(options)**(n-1)
#
  #change = 0
  #for y in range(0, len(options)):
  #  for i in range(0, len(options)):
  #    for j in range(0, len(options)**(n-2)):   # The amount of times each option should appear in a specified position
  #      answer[j + change][1] = options[i]
  #        #if(len(answer) == 1):
  #        #  answer[i] = options[j]
  #        #else:
  #    change += len(options)**(n-2)
#
  #change = 0
  #for z in range(0, len(options)):
  #  for y in range(0, len(options)):
  #    for i in range(0, len(options)):
  #      for j in range(0, len(options)**(n-3)):   # The amount of times each option should appear in a specified position
  #        answer[j + change][2] = options[i]
  #          #if(len(answer) == 1):
  #          #  answer[i] = options[j]
  #          #else:
  #      change += len(options)**(n-3)
  
  x = n
  while x > 0:
    change = 0
    for z in range(0, len(options)**(x - 1)): #extra options loop
      for i in range(0, len(options)):
        for j in range(0, len(options)**(n - x)):
          answer[j + change][x-1] = options[i]
        change += len(options)**(n-x)
    x -= 1

  return answer

#print(rock_paper_scissors(2))
#
#
#  for combo in answer:
#    for option in combo:
#      option = 'rock'
#
#  for i in range(0, len(answer)):
#    for j in range(0, len(answer[i])):
#      answer[i][j] = options[j]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')