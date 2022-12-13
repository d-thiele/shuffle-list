import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('--file', required=True, type=argparse.FileType('r'))
args = parser.parse_args()
inputfile = args.file

lines = inputfile.readlines()
random.shuffle(lines)
[print(line.strip()) for line in lines]
