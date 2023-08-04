import sys
import argparse
import json 

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

parser = argparse.ArgumentParser()

parser.add_argument('--myArg1',dest="a1")
parser.add_argument('--myArg2', dest="a2")
known_args,new_args = parser.parse_known_args()

print(known_args)
print(new_args)


print(json.loads(known_args.a1))
print(json.loads(known_args.a2))
