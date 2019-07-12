#!/bin/sh
#$ -cwd
#$ -N cdhit-est
module load singularity
singularity exec /usr/local/biotools/c/cd-hit:4.6.8--0 cd-hit-est -i /home/kumay/metagenome_data/clusterd_genes/clusterd_over500_over100_with_TARA.fa -o /home/kumay/metagenome_data/clusterd_genes/clustered_genes_with_tara_2d_mod_optioni_est -c 0.9 -T 0 -M 0 -G 0 -aS 0.85 -aL 0.85 -g 1 -r 1 -d 0 
 

