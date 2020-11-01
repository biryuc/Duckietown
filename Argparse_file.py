import argparse
parser = argparse.ArgumentParser(description='Simple search in file!!!')
parser.add_argument('--l', help='longest str')
parser.add_argument('--com', help='The most common word')
parser.add_argument('--cc', help='The most common character')
args = parser.parse_args()
file = open("file.txt")
s = file.read()


for line in file:

    print(line)