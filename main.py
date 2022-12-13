import argparse
import random
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--file', required=True, type=argparse.FileType('r'))
parser.add_argument('--buckets', required=True, type=int)
args = parser.parse_args()
inputfile = args.file
buckets = args.buckets

lines = inputfile.readlines()
random.shuffle(lines)

if buckets > len(lines):
    print('There are fewer lines in the file than buckets to divide them into. Try again. Exitting.')
    sys.exit(1)
elif buckets > 1:
    pass
    # get number of lines to put in each bucket
    floor = len(lines) // buckets
    modulo = len(lines) % buckets
    print(f'lines count is {len(lines)}, buckets is {buckets}, floor is {floor}, modulo is {modulo}')
    bucket_lengths = {}
    for bucket in range(buckets):
        # print(f'starting bucket {bucket} with floor of {floor} and modulo of {modulo}')
        if modulo != 0:
            increased_amt_for_bucket = floor + 1
            #print(f'increased amount for this bucket due to non-zero modulo is {increased_amt_for_bucket}')
            bucket_lengths[bucket] = increased_amt_for_bucket
            modulo -= 1
            continue
        if modulo == 0:
            bucket_lengths[bucket] = floor
            continue
    print(f'bucket_lengths is {bucket_lengths}')
    # put lines in each bucket
    bucket_items = {}
    start = 0
    for bucket in range(buckets):
        end = start + bucket_lengths[bucket]
        bucket_items[bucket] = lines[start: end]
        # print the lines for all the buckets
        print(f'\nbucket {bucket} has the following members:\n')
        [print(line.strip()) for line in bucket_items[bucket]]
        start = end
elif buckets == 1:
    [print(line.strip()) for line in lines]
else:
    print('No negative numbers please. Exitting.')
    sys.exit(1)
