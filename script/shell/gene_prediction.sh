#!/bin/sh
#$ -cwd
#$ -N gene_prediction_over500 
/home/kumay/software/Prodigal/prodigal  -i final.contigs_over500.fa -d my.proteins_over500_meta.fna -o my.genes_over500_meta -a my.proteins_over500_meta.faa -p meta -q

