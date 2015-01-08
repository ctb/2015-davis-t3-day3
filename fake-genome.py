import random

dna = ["A", "C", "G", "T"]
dna = dna*250
random.shuffle(dna)

print '>genome'
print "".join(dna)
