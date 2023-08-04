import sys
import argparse

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

parser = argparse.ArgumentParser()

parser.add_argument('--myArg1')
parser.add_argument('--myArg2')
known_args,new_args = parser.parse_known_args()

print(known_args)
print(new_args)
