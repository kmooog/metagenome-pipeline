#!/bin/sh
#$ -cwd
#$ -N cdhit
module load singularity
singularity exec /usr/local/biotools/c/cd-hit:4.6.8--0 cd-hit-est-2d -i2 /home/kumay/metagenome_data/all_assembled_gene_prediction/my.proteins_over500.fna -i /home/kumay/tara_data/OM-RGC.fa -o /home/kumay/metagenome_data/clusterd_genes/clustered_genes_with_tara_2d_reverse -c 0.95 -T 0 -M 0 -G 0 -aS 0.9 -g 1 -r 1 -d 0 
 

