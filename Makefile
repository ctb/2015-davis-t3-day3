all: genome.fa reads.fa error-hist.csv

clean:
	-rm genome.fa

genome.fa: fake-genome.py
	python fake-genome.py  > genome.fa

reads.fa: genome.fa make-reads.py
	python make-reads.py genome.fa > reads.fa

error-hist.csv: reads.fa calc-error-spectrum.py
	python calc-error-spectrum.py reads.fa > error-hist.csv
