import khmer
import sys
import screed

CUTOFF=10

kh = khmer.new_counting_hash(20, 1e6, 4)
kh.consume_fasta(sys.argv[1])

hist = [0]*1000
        
for n, record in enumerate(screed.open(sys.argv[1])):
    positions = kh.find_spectral_error_positions(\
        record.sequence, CUTOFF)

    for pos in positions:
        hist[pos] += 1

LAST_ZERO = len(hist) - 1
while 1:
    if hist[LAST_ZERO] != 0:
        break
    LAST_ZERO -= 1

for n, count in enumerate(hist[:LAST_ZERO]):
    print "%d,%d" % (n, count,)
