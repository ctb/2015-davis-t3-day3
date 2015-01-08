all: genome.fa

clean:
	-rm genome.fa

genome.fa:
	python fake-genome.py  > genome.fa
