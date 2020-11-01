#!/bin/bash
# file = open("/home/nikita/OperationSystems/Five.txt", "r")
# i = 0
# for line in file:
#     i = i + 1
#
# print(i)
# file_1 = open("file.txt", "w")
# file_1.write(str(i))
#----------------------------
# i = 0
# while True:
#     name = input("Enter your name:")
#     birth_day = input("Enter your birth_day day/month/year:")
#     file = open("file.txt", "a")
#     i = i + 1
#     b = str(i)
#     file.write(b + " " + name + " " + birth_day)
#     file.write('\n')
#
#     print(i)
# --------------------------------
import argparse


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))