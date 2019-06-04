#!/bin/sh
#$ -cwd
#$ -N meta_assemble
/home/kumay/software/Prodigal/prodigal  -i final.contigs.fa -o my.genes -a my.proteins.faa -p meta -q

