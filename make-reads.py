import sys
import screed
import random

N=1000
L=100

genomefile = sys.argv[1]

for record in screed.open(genomefile):
    genome = record.sequence

for i in range(N):
    start = random.randint(0, len(genome) - 1 - L)
    end = start + L
    read = genome[start:end]

    if random.choice([0,1]):
        read = screed.rc(read)

    assert len(read) == L
    print '>read%d\n%s' % (i, read)
