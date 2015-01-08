import sys
import screed
import random
import argparse

N=1000
L=100

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('genomefile')
    parser.add_argument('--error', type=int)
    args = parser.parse_args()

    genomefile = args.genomefile

    for record in screed.open(genomefile):
        genome = record.sequence

    for i in range(N):
        start = random.randint(0, len(genome) - 1 - L)
        end = start + L
        read = genome[start:end]

        for _ in range(L):
            if random.randint(0, args.error) == 0:
                position = random.randint(0, L - 1)
                newbase = random.choice(["a", "c", "g", "t"])
                read = read[:position] + newbase + \
                       read[position+1:]

        if random.choice([0,1]):
            read = screed.rc(read)

        assert len(read) == L
        print '>read%d\n%s' % (i, read)

if __name__ == '__main__':
    main()
