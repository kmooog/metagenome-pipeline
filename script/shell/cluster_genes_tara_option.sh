#!/bin/sh  
#$ -cwd      
#$ -N cdhit   

/home/kumay/software/cd-hit-v4.8.1-2019-0228/cd-hit-est -i /home/kumay/metagenome_data/all_assembled_gene_prediction/my.proteins.fna -o /home/kumay/metagenome_data/all_assembled_gene_prediction/clusterd_genes_para.fna --Q 8 -c 0.95 -T 0 -M 0 -G 0 -aS 0.9 -g 1 -r 1 -d 0 
