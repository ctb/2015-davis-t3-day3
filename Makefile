all: genome.fa reads.fa

clean:
	-rm genome.fa

genome.fa: fake-genome.py
	python fake-genome.py  > genome.fa

reads.fa: genome.fa make-reads.py
	python make-reads.py genome.fa > reads.fa
