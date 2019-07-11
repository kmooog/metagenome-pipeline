#!/bin/sh
#$ -cwd
#$ -N cdhit
module load singularity
singularity exec /usr/local/biotools/c/cd-hit:4.6.8--0 cd-hit-est-2d -i2 /home/kumay/metagenome_data/all_assembled_gene_prediction/my.proteins_over500_over100.fna -i /home/kumay/tara_data/OM-RGC.fa -o /home/kumay/metagenome_data/clusterd_genes/clustered_genes_with_tara_2d_mod_option_rev -c 0.9 -T 0 -M 0 -G 0 -s2 0.85 -aS 0.85 -aL 0.85 -g 1 -r 1 -d 0 
 

