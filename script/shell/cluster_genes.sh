#!/bin/sh
#$ -cwd
#$ -N cdhit
module load singularity
singularity exec /usr/local/biotools/c/cd-hit:4.6.8--0 cd-hit-est -i /home/kumay/metagenome_data/all_assembled_gene_prediction_20190718/my.proteins_over500_over100_meta.fna -o /home/kumay/metagenome_data/all_assembled_gene_prediction_20190718/clusterd_over500_over100 -c 0.95 -T 0 -M 0 -G 0 -aS 0.9 -g 1 -r 1 -d 0 
 

